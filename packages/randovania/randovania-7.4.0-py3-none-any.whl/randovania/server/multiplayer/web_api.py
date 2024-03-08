import construct
import flask
from playhouse import flask_utils

from randovania.game_description import default_database
from randovania.layout.versioned_preset import VersionedPreset
from randovania.network_common import remote_inventory
from randovania.server.database import MultiplayerSession, World, WorldUserAssociation
from randovania.server.server_app import ServerApp


def admin_sessions(user):
    paginated_query = flask_utils.PaginatedQuery(
        MultiplayerSession.select().order_by(MultiplayerSession.creation_date.desc()),
        paginate_by=20,
        check_bounds=True,
    )

    lines = []
    for session in paginated_query.get_object_list():
        assert isinstance(session, MultiplayerSession)
        lines.append(
            "<tr>{}</tr>".format(
                "".join(
                    f"<td>{col}</td>"
                    for col in [
                        "<a href='{}'>{}</a>".format(
                            flask.url_for("admin_session", session_id=session.id),
                            session.name,
                        ),
                        session.creator.name,
                        session.creation_date,
                        len(session.members),
                        len(session.worlds),
                    ]
                )
            )
        )

    page = paginated_query.get_page()
    previous = "Previous"
    if page > 1:
        previous = "<a href='{}'>Previous</a>".format(flask.url_for(".admin_sessions", page=page - 1))

    next_link = "Next"
    if page < paginated_query.get_page_count():
        next_link = "<a href='{}'>Next</a>".format(flask.url_for(".admin_sessions", page=page + 1))

    header = ["Name", "Creator", "Creation Date", "Num Users", "Num Worlds"]
    return (
        "<table border='1'><tr>{header}</tr>{content}</table>Page {page} of {num_pages}. {previous} / {next}."
    ).format(
        header="".join(f"<th>{it}</th>" for it in header),
        content="".join(lines),
        page=page,
        num_pages=paginated_query.get_page_count(),
        previous=previous,
        next=next_link,
    )


def admin_session(user, session_id):
    session: MultiplayerSession = MultiplayerSession.get_by_id(session_id)
    rows = []

    associations: list[WorldUserAssociation] = list(
        WorldUserAssociation.select()
        .join(World)
        .where(
            World.session == session,
        )
    )

    for association in associations:
        inventory = []

        if association.inventory is not None:
            parsed_inventory = remote_inventory.decode_remote_inventory(association.inventory)

            if isinstance(parsed_inventory, construct.ConstructError):
                inventory.append(f"Error parsing: {parsed_inventory}")
            else:
                game = VersionedPreset.from_str(association.world.preset).game
                db = default_database.resource_database_for(game)
                for item_name, item in parsed_inventory.items():
                    if item > 0:
                        inventory.append(f"{db.get_item(item_name).long_name} x{item}")
        else:
            inventory.append("Missing")

        rows.append(
            [
                association.user.name,
                association.world.name,
                association.connection_state.pretty_text,
                ", ".join(inventory),
            ]
        )

    header = ["User", "World", "Connection State", "Inventory"]

    return "<table border='1'><tr>{}</tr>{}</table>".format(
        "".join(f"<th>{h}</th>" for h in header),
        "".join("<tr>{}</tr>".format("".join(f"<td>{h}</td>" for h in r)) for r in rows),
    )


def setup_app(sa: ServerApp):
    sa.route_with_user("/sessions", need_admin=True)(admin_sessions)
    sa.route_with_user("/session/<session_id>", need_admin=True)(admin_session)
