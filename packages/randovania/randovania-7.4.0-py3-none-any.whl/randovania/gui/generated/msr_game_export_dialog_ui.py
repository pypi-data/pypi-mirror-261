# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'msr_game_export_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

class Ui_MSRGameExportDialog(object):
    def setupUi(self, MSRGameExportDialog):
        if not MSRGameExportDialog.objectName():
            MSRGameExportDialog.setObjectName(u"MSRGameExportDialog")
        MSRGameExportDialog.resize(493, 458)
        self.root_layout = QGridLayout(MSRGameExportDialog)
        self.root_layout.setSpacing(6)
        self.root_layout.setContentsMargins(11, 11, 11, 11)
        self.root_layout.setObjectName(u"root_layout")
        self.output_tab_widget = QTabWidget(MSRGameExportDialog)
        self.output_tab_widget.setObjectName(u"output_tab_widget")
        self.tab_sd_card = QWidget()
        self.tab_sd_card.setObjectName(u"tab_sd_card")
        self.verticalLayout = QVBoxLayout(self.tab_sd_card)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.sd_label = QLabel(self.tab_sd_card)
        self.sd_label.setObjectName(u"sd_label")

        self.verticalLayout.addWidget(self.sd_label)

        self.sd_driver_layout = QHBoxLayout()
        self.sd_driver_layout.setSpacing(6)
        self.sd_driver_layout.setObjectName(u"sd_driver_layout")
        self.sd_combo = QComboBox(self.tab_sd_card)
        self.sd_combo.addItem("")
        self.sd_combo.setObjectName(u"sd_combo")

        self.sd_driver_layout.addWidget(self.sd_combo)

        self.sd_non_removable = QCheckBox(self.tab_sd_card)
        self.sd_non_removable.setObjectName(u"sd_non_removable")

        self.sd_driver_layout.addWidget(self.sd_non_removable)

        self.sd_refresh_button = QPushButton(self.tab_sd_card)
        self.sd_refresh_button.setObjectName(u"sd_refresh_button")

        self.sd_driver_layout.addWidget(self.sd_refresh_button)


        self.verticalLayout.addLayout(self.sd_driver_layout)

        self.output_tab_widget.addTab(self.tab_sd_card, "")
        self.tab_ftp = QWidget()
        self.tab_ftp.setObjectName(u"tab_ftp")
        self.tab_ftp_layout = QGridLayout(self.tab_ftp)
        self.tab_ftp_layout.setSpacing(6)
        self.tab_ftp_layout.setContentsMargins(11, 11, 11, 11)
        self.tab_ftp_layout.setObjectName(u"tab_ftp_layout")
        self.ftp_description_label = QLabel(self.tab_ftp)
        self.ftp_description_label.setObjectName(u"ftp_description_label")
        self.ftp_description_label.setWordWrap(True)
        self.ftp_description_label.setOpenExternalLinks(True)

        self.tab_ftp_layout.addWidget(self.ftp_description_label, 0, 0, 1, 4)

        self.ftp_anonymous_check = QCheckBox(self.tab_ftp)
        self.ftp_anonymous_check.setObjectName(u"ftp_anonymous_check")

        self.tab_ftp_layout.addWidget(self.ftp_anonymous_check, 1, 0, 1, 1)

        self.ftp_username_edit = QLineEdit(self.tab_ftp)
        self.ftp_username_edit.setObjectName(u"ftp_username_edit")

        self.tab_ftp_layout.addWidget(self.ftp_username_edit, 1, 1, 1, 1)

        self.ftp_password_edit = QLineEdit(self.tab_ftp)
        self.ftp_password_edit.setObjectName(u"ftp_password_edit")

        self.tab_ftp_layout.addWidget(self.ftp_password_edit, 1, 2, 1, 2)

        self.ftp_ip_label = QLabel(self.tab_ftp)
        self.ftp_ip_label.setObjectName(u"ftp_ip_label")

        self.tab_ftp_layout.addWidget(self.ftp_ip_label, 2, 0, 1, 1)

        self.ftp_ip_edit = QLineEdit(self.tab_ftp)
        self.ftp_ip_edit.setObjectName(u"ftp_ip_edit")

        self.tab_ftp_layout.addWidget(self.ftp_ip_edit, 2, 1, 1, 1)

        self.ftp_port_edit = QLineEdit(self.tab_ftp)
        self.ftp_port_edit.setObjectName(u"ftp_port_edit")
        self.ftp_port_edit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.tab_ftp_layout.addWidget(self.ftp_port_edit, 2, 2, 1, 1)

        self.ftp_test_button = QPushButton(self.tab_ftp)
        self.ftp_test_button.setObjectName(u"ftp_test_button")

        self.tab_ftp_layout.addWidget(self.ftp_test_button, 2, 3, 1, 1)

        self.output_tab_widget.addTab(self.tab_ftp, "")
        self.tab_citra = QWidget()
        self.tab_citra.setObjectName(u"tab_citra")
        self.citra_label = QLabel(self.tab_citra)
        self.citra_label.setObjectName(u"citra_label")
        self.citra_label.setGeometry(QRect(0, 0, 473, 71))
        self.citra_label.setWordWrap(True)
        self.output_tab_widget.addTab(self.tab_citra, "")
        self.tab_custom_path = QWidget()
        self.tab_custom_path.setObjectName(u"tab_custom_path")
        self.gridLayout_3 = QGridLayout(self.tab_custom_path)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.custom_path_edit = QLineEdit(self.tab_custom_path)
        self.custom_path_edit.setObjectName(u"custom_path_edit")

        self.gridLayout_3.addWidget(self.custom_path_edit, 1, 0, 1, 1)

        self.custom_path_button = QPushButton(self.tab_custom_path)
        self.custom_path_button.setObjectName(u"custom_path_button")
        self.custom_path_button.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_3.addWidget(self.custom_path_button, 1, 1, 1, 1)

        self.custom_path_label = QLabel(self.tab_custom_path)
        self.custom_path_label.setObjectName(u"custom_path_label")
        self.custom_path_label.setWordWrap(True)

        self.gridLayout_3.addWidget(self.custom_path_label, 0, 0, 1, 2)

        self.output_tab_widget.addTab(self.tab_custom_path, "")

        self.root_layout.addWidget(self.output_tab_widget, 6, 0, 2, 3)

        self.cancel_button = QPushButton(MSRGameExportDialog)
        self.cancel_button.setObjectName(u"cancel_button")

        self.root_layout.addWidget(self.cancel_button, 10, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.root_layout.addItem(self.verticalSpacer, 5, 0, 1, 3)

        self.input_file_button = QPushButton(MSRGameExportDialog)
        self.input_file_button.setObjectName(u"input_file_button")
        self.input_file_button.setMaximumSize(QSize(100, 16777215))

        self.root_layout.addWidget(self.input_file_button, 2, 2, 1, 1)

        self.line = QFrame(MSRGameExportDialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.root_layout.addWidget(self.line, 3, 0, 1, 3)

        self.input_file_label = QLabel(MSRGameExportDialog)
        self.input_file_label.setObjectName(u"input_file_label")
        self.input_file_label.setMaximumSize(QSize(16777215, 20))

        self.root_layout.addWidget(self.input_file_label, 1, 0, 1, 2)

        self.input_file_edit = QLineEdit(MSRGameExportDialog)
        self.input_file_edit.setObjectName(u"input_file_edit")

        self.root_layout.addWidget(self.input_file_edit, 2, 0, 1, 2)

        self.description_label = QLabel(MSRGameExportDialog)
        self.description_label.setObjectName(u"description_label")
        self.description_label.setWordWrap(True)

        self.root_layout.addWidget(self.description_label, 0, 0, 1, 3)

        self.accept_button = QPushButton(MSRGameExportDialog)
        self.accept_button.setObjectName(u"accept_button")

        self.root_layout.addWidget(self.accept_button, 10, 0, 1, 1)

        self.target_platform_layout = QHBoxLayout()
        self.target_platform_layout.setSpacing(6)
        self.target_platform_layout.setObjectName(u"target_platform_layout")
        self.target_platform_label = QLabel(MSRGameExportDialog)
        self.target_platform_label.setObjectName(u"target_platform_label")

        self.target_platform_layout.addWidget(self.target_platform_label)

        self.luma_radio = QRadioButton(MSRGameExportDialog)
        self.platform_btn_group = QButtonGroup(MSRGameExportDialog)
        self.platform_btn_group.setObjectName(u"platform_btn_group")
        self.platform_btn_group.addButton(self.luma_radio)
        self.luma_radio.setObjectName(u"luma_radio")

        self.target_platform_layout.addWidget(self.luma_radio)

        self.citra_radio = QRadioButton(MSRGameExportDialog)
        self.platform_btn_group.addButton(self.citra_radio)
        self.citra_radio.setObjectName(u"citra_radio")

        self.target_platform_layout.addWidget(self.citra_radio)


        self.root_layout.addLayout(self.target_platform_layout, 4, 0, 1, 3)

        self.auto_save_spoiler_check = QCheckBox(MSRGameExportDialog)
        self.auto_save_spoiler_check.setObjectName(u"auto_save_spoiler_check")

        self.root_layout.addWidget(self.auto_save_spoiler_check, 9, 0, 1, 1)

        self.version_layout = QHBoxLayout()
        self.version_layout.setSpacing(6)
        self.version_layout.setObjectName(u"version_layout")
        self.version_label = QLabel(MSRGameExportDialog)
        self.version_label.setObjectName(u"version_label")

        self.version_layout.addWidget(self.version_label)

        self.ntsc_radio = QRadioButton(MSRGameExportDialog)
        self.version_btn_group = QButtonGroup(MSRGameExportDialog)
        self.version_btn_group.setObjectName(u"version_btn_group")
        self.version_btn_group.addButton(self.ntsc_radio)
        self.ntsc_radio.setObjectName(u"ntsc_radio")

        self.version_layout.addWidget(self.ntsc_radio)

        self.pal_radio = QRadioButton(MSRGameExportDialog)
        self.version_btn_group.addButton(self.pal_radio)
        self.pal_radio.setObjectName(u"pal_radio")

        self.version_layout.addWidget(self.pal_radio)


        self.root_layout.addLayout(self.version_layout, 5, 0, 1, 3)


        self.retranslateUi(MSRGameExportDialog)

        self.output_tab_widget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MSRGameExportDialog)
    # setupUi

    def retranslateUi(self, MSRGameExportDialog):
        MSRGameExportDialog.setWindowTitle(QCoreApplication.translate("MSRGameExportDialog", u"Game Patching", None))
        self.sd_label.setText(QCoreApplication.translate("MSRGameExportDialog", u"Select the driver letter for your SD Card", None))
        self.sd_combo.setItemText(0, QCoreApplication.translate("MSRGameExportDialog", u"D:", None))

        self.sd_non_removable.setText(QCoreApplication.translate("MSRGameExportDialog", u"Show non-removable", None))
        self.sd_refresh_button.setText(QCoreApplication.translate("MSRGameExportDialog", u"Refresh", None))
        self.output_tab_widget.setTabText(self.output_tab_widget.indexOf(self.tab_sd_card), QCoreApplication.translate("MSRGameExportDialog", u"SD Card", None))
        self.ftp_description_label.setText(QCoreApplication.translate("MSRGameExportDialog", u"<html><head/><body><p>Upload the exported mod directly to your 3DS, via FTP, to a path compatible with Luma.</p><p>In order to provide a FTP server in your 3DS, run <a href=\"https://github.com/mtheall/ftpd\"><span style=\" text-decoration: underline; color:#007af4;\">ftpd</span></a> or download it directly from the homebrew store.</p></body></html>", None))
        self.ftp_anonymous_check.setText(QCoreApplication.translate("MSRGameExportDialog", u"Anonymous", None))
        self.ftp_username_edit.setPlaceholderText(QCoreApplication.translate("MSRGameExportDialog", u"Username", None))
        self.ftp_password_edit.setPlaceholderText(QCoreApplication.translate("MSRGameExportDialog", u"Password", None))
        self.ftp_ip_label.setText(QCoreApplication.translate("MSRGameExportDialog", u"3DS IP", None))
        self.ftp_port_edit.setText(QCoreApplication.translate("MSRGameExportDialog", u"21", None))
        self.ftp_test_button.setText(QCoreApplication.translate("MSRGameExportDialog", u"Test connection", None))
        self.output_tab_widget.setTabText(self.output_tab_widget.indexOf(self.tab_ftp), QCoreApplication.translate("MSRGameExportDialog", u"Upload via FTP", None))
        self.citra_label.setText(QCoreApplication.translate("MSRGameExportDialog", u"<html><head/><body><p>The game will be exported directly to Citra's mod folder for Metroid: Samus Returns.</p><p>Path to be used:<br/><span style=\" font-size:8pt;\">{mod_path}</span></p><p>Please make sure Citra is closed before exporting a game.</p></body></html>", None))
        self.output_tab_widget.setTabText(self.output_tab_widget.indexOf(self.tab_citra), QCoreApplication.translate("MSRGameExportDialog", u"Citra", None))
        self.custom_path_edit.setPlaceholderText(QCoreApplication.translate("MSRGameExportDialog", u"Path where to place randomized game", None))
        self.custom_path_button.setText(QCoreApplication.translate("MSRGameExportDialog", u"Select File", None))
        self.custom_path_label.setText(QCoreApplication.translate("MSRGameExportDialog", u"<html><head/><body><p>Saves the mod to a path or your choosing, leaving the responsibility of placing the files in the correct location to you.</p><p>This path and input path are not allowed to contain the other.</p><p>It's recommended to use one of the other options.</p></body></html>", None))
        self.output_tab_widget.setTabText(self.output_tab_widget.indexOf(self.tab_custom_path), QCoreApplication.translate("MSRGameExportDialog", u"Custom Path", None))
        self.cancel_button.setText(QCoreApplication.translate("MSRGameExportDialog", u"Cancel", None))
        self.input_file_button.setText(QCoreApplication.translate("MSRGameExportDialog", u"Select File", None))
        self.input_file_label.setText(QCoreApplication.translate("MSRGameExportDialog", u"Input Path (Unmodified Samus Returns extracted RomFS)", None))
        self.input_file_edit.setPlaceholderText(QCoreApplication.translate("MSRGameExportDialog", u"Path to vanilla extracted RomFS", None))
        self.description_label.setText(QCoreApplication.translate("MSRGameExportDialog", u"<html><head/><body><p>In order to create the randomized game, an extracted RomFS of Metroid: Samus Returns for the Nintendo 3DS is necessary.</p></body></html>", None))
        self.accept_button.setText(QCoreApplication.translate("MSRGameExportDialog", u"Accept", None))
        self.target_platform_label.setText(QCoreApplication.translate("MSRGameExportDialog", u"Target Platform", None))
        self.luma_radio.setText(QCoreApplication.translate("MSRGameExportDialog", u"Luma3DS", None))
#if QT_CONFIG(tooltip)
        self.citra_radio.setToolTip(QCoreApplication.translate("MSRGameExportDialog", u"<html><head/><body><p>Randovania only supports Citra.</p><p>Use other emulators at your own risk, but do not report any issues.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.citra_radio.setText(QCoreApplication.translate("MSRGameExportDialog", u"Citra", None))
        self.auto_save_spoiler_check.setText(QCoreApplication.translate("MSRGameExportDialog", u"Include a spoiler log on same directory", None))
        self.version_label.setText(QCoreApplication.translate("MSRGameExportDialog", u"Version", None))
        self.ntsc_radio.setText(QCoreApplication.translate("MSRGameExportDialog", u"NTSC", None))
        self.pal_radio.setText(QCoreApplication.translate("MSRGameExportDialog", u"PAL", None))
    # retranslateUi

