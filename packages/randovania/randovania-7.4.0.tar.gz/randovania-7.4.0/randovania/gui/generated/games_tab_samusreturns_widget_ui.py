# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'games_tab_samusreturns_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from randovania.gui.widgets.generate_game_widget import *  # type: ignore

class Ui_SamusReturnsGameTabWidget(object):
    def setupUi(self, SamusReturnsGameTabWidget):
        if not SamusReturnsGameTabWidget.objectName():
            SamusReturnsGameTabWidget.setObjectName(u"SamusReturnsGameTabWidget")
        SamusReturnsGameTabWidget.resize(671, 675)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SamusReturnsGameTabWidget.sizePolicy().hasHeightForWidth())
        SamusReturnsGameTabWidget.setSizePolicy(sizePolicy)
        self.tab_intro = QWidget()
        self.tab_intro.setObjectName(u"tab_intro")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tab_intro.sizePolicy().hasHeightForWidth())
        self.tab_intro.setSizePolicy(sizePolicy1)
        self.intro_layout = QVBoxLayout(self.tab_intro)
        self.intro_layout.setSpacing(6)
        self.intro_layout.setContentsMargins(11, 11, 11, 11)
        self.intro_layout.setObjectName(u"intro_layout")
        self.intro_layout.setSizeConstraint(QLayout.SetMinimumSize)
        self.intro_cover_layout = QHBoxLayout()
        self.intro_cover_layout.setSpacing(6)
        self.intro_cover_layout.setObjectName(u"intro_cover_layout")
        self.game_cover_label = QLabel(self.tab_intro)
        self.game_cover_label.setObjectName(u"game_cover_label")

        self.intro_cover_layout.addWidget(self.game_cover_label)

        self.intro_label = QLabel(self.tab_intro)
        self.intro_label.setObjectName(u"intro_label")
        sizePolicy1.setHeightForWidth(self.intro_label.sizePolicy().hasHeightForWidth())
        self.intro_label.setSizePolicy(sizePolicy1)
        self.intro_label.setWordWrap(True)

        self.intro_cover_layout.addWidget(self.intro_label)


        self.intro_layout.addLayout(self.intro_cover_layout)

        self.quick_generate_button = QPushButton(self.tab_intro)
        self.quick_generate_button.setObjectName(u"quick_generate_button")

        self.intro_layout.addWidget(self.quick_generate_button)

        self.intro_spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.intro_layout.addItem(self.intro_spacer)

        SamusReturnsGameTabWidget.addTab(self.tab_intro, "")
        self.tab_generate_game = GenerateGameWidget()
        self.tab_generate_game.setObjectName(u"tab_generate_game")
        SamusReturnsGameTabWidget.addTab(self.tab_generate_game, "")
        self.faq_tab = QWidget()
        self.faq_tab.setObjectName(u"faq_tab")
        self.faq_layout = QGridLayout(self.faq_tab)
        self.faq_layout.setSpacing(6)
        self.faq_layout.setContentsMargins(11, 11, 11, 11)
        self.faq_layout.setObjectName(u"faq_layout")
        self.faq_layout.setContentsMargins(0, 0, 0, 0)
        self.faq_scroll_area = QScrollArea(self.faq_tab)
        self.faq_scroll_area.setObjectName(u"faq_scroll_area")
        self.faq_scroll_area.setWidgetResizable(True)
        self.faq_scroll_area_contents = QWidget()
        self.faq_scroll_area_contents.setObjectName(u"faq_scroll_area_contents")
        self.faq_scroll_area_contents.setGeometry(QRect(0, 0, 665, 646))
        self.gridLayout_8 = QGridLayout(self.faq_scroll_area_contents)
        self.gridLayout_8.setSpacing(6)
        self.gridLayout_8.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.faq_label = QLabel(self.faq_scroll_area_contents)
        self.faq_label.setObjectName(u"faq_label")
        self.faq_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.faq_label.setWordWrap(True)

        self.gridLayout_8.addWidget(self.faq_label, 0, 0, 1, 1)

        self.faq_scroll_area.setWidget(self.faq_scroll_area_contents)

        self.faq_layout.addWidget(self.faq_scroll_area, 0, 0, 1, 1)

        SamusReturnsGameTabWidget.addTab(self.faq_tab, "")
        self.differences_tab = QScrollArea()
        self.differences_tab.setObjectName(u"differences_tab")
        self.differences_tab.setWidgetResizable(True)
        self.differences_contents = QWidget()
        self.differences_contents.setObjectName(u"differences_contents")
        self.differences_contents.setGeometry(QRect(0, 0, 651, 1052))
        self.verticalLayout = QVBoxLayout(self.differences_contents)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.differences_label = QLabel(self.differences_contents)
        self.differences_label.setObjectName(u"differences_label")
        self.differences_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.differences_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.differences_label)

        self.differences_tab.setWidget(self.differences_contents)
        SamusReturnsGameTabWidget.addTab(self.differences_tab, "")
        self.hints_tab = QWidget()
        self.hints_tab.setObjectName(u"hints_tab")
        self.gridLayout = QGridLayout(self.hints_tab)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.hints_scroll_area = QScrollArea(self.hints_tab)
        self.hints_scroll_area.setObjectName(u"hints_scroll_area")
        self.hints_scroll_area.setWidgetResizable(True)
        self.hints_scroll_area_contents = QWidget()
        self.hints_scroll_area_contents.setObjectName(u"hints_scroll_area_contents")
        self.hints_scroll_area_contents.setGeometry(QRect(0, 0, 665, 646))
        self.verticalLayout_2 = QVBoxLayout(self.hints_scroll_area_contents)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.hints_label = QLabel(self.hints_scroll_area_contents)
        self.hints_label.setObjectName(u"hints_label")
        self.hints_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.hints_label.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.hints_label)

        self.line = QFrame(self.hints_scroll_area_contents)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.hints_label_2 = QLabel(self.hints_scroll_area_contents)
        self.hints_label_2.setObjectName(u"hints_label_2")
        self.hints_label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.hints_label_2.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.hints_label_2)

        self.hints_dna_locations_widget = QTableWidget(self.hints_scroll_area_contents)
        if (self.hints_dna_locations_widget.columnCount() < 2):
            self.hints_dna_locations_widget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.hints_dna_locations_widget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.hints_dna_locations_widget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.hints_dna_locations_widget.rowCount() < 10):
            self.hints_dna_locations_widget.setRowCount(10)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.hints_dna_locations_widget.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.hints_dna_locations_widget.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.hints_dna_locations_widget.setVerticalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.hints_dna_locations_widget.setVerticalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.hints_dna_locations_widget.setVerticalHeaderItem(4, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.hints_dna_locations_widget.setVerticalHeaderItem(5, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.hints_dna_locations_widget.setVerticalHeaderItem(6, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.hints_dna_locations_widget.setVerticalHeaderItem(7, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.hints_dna_locations_widget.setVerticalHeaderItem(8, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.hints_dna_locations_widget.setVerticalHeaderItem(9, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignCenter);
        self.hints_dna_locations_widget.setItem(0, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter);
        self.hints_dna_locations_widget.setItem(0, 1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignCenter);
        self.hints_dna_locations_widget.setItem(1, 0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setTextAlignment(Qt.AlignCenter);
        self.hints_dna_locations_widget.setItem(1, 1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setTextAlignment(Qt.AlignCenter);
        self.hints_dna_locations_widget.setItem(2, 0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setTextAlignment(Qt.AlignCenter);
        self.hints_dna_locations_widget.setItem(2, 1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setTextAlignment(Qt.AlignCenter);
        self.hints_dna_locations_widget.setItem(3, 0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setTextAlignment(Qt.AlignCenter);
        self.hints_dna_locations_widget.setItem(3, 1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setTextAlignment(Qt.AlignCenter);
        self.hints_dna_locations_widget.setItem(4, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setTextAlignment(Qt.AlignCenter);
        self.hints_dna_locations_widget.setItem(4, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setTextAlignment(Qt.AlignCenter);
        self.hints_dna_locations_widget.setItem(5, 0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setTextAlignment(Qt.AlignCenter);
        self.hints_dna_locations_widget.setItem(5, 1, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setTextAlignment(Qt.AlignCenter);
        self.hints_dna_locations_widget.setItem(6, 0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setTextAlignment(Qt.AlignCenter);
        self.hints_dna_locations_widget.setItem(6, 1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setTextAlignment(Qt.AlignCenter);
        self.hints_dna_locations_widget.setItem(7, 0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setTextAlignment(Qt.AlignCenter);
        self.hints_dna_locations_widget.setItem(7, 1, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setTextAlignment(Qt.AlignCenter);
        self.hints_dna_locations_widget.setItem(8, 0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setTextAlignment(Qt.AlignCenter);
        self.hints_dna_locations_widget.setItem(8, 1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setTextAlignment(Qt.AlignCenter);
        self.hints_dna_locations_widget.setItem(9, 0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setTextAlignment(Qt.AlignCenter);
        self.hints_dna_locations_widget.setItem(9, 1, __qtablewidgetitem31)
        self.hints_dna_locations_widget.setObjectName(u"hints_dna_locations_widget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.hints_dna_locations_widget.sizePolicy().hasHeightForWidth())
        self.hints_dna_locations_widget.setSizePolicy(sizePolicy2)
        self.hints_dna_locations_widget.setMinimumSize(QSize(0, 339))
        self.hints_dna_locations_widget.setAutoFillBackground(False)
        self.hints_dna_locations_widget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.hints_dna_locations_widget.setAutoScroll(True)
        self.hints_dna_locations_widget.setAlternatingRowColors(True)
        self.hints_dna_locations_widget.setSortingEnabled(True)
        self.hints_dna_locations_widget.setRowCount(10)
        self.hints_dna_locations_widget.setColumnCount(2)
        self.hints_dna_locations_widget.horizontalHeader().setVisible(True)
        self.hints_dna_locations_widget.horizontalHeader().setCascadingSectionResizes(False)
        self.hints_dna_locations_widget.horizontalHeader().setMinimumSectionSize(30)
        self.hints_dna_locations_widget.horizontalHeader().setDefaultSectionSize(322)
        self.hints_dna_locations_widget.horizontalHeader().setProperty("showSortIndicator", False)
        self.hints_dna_locations_widget.horizontalHeader().setStretchLastSection(False)
        self.hints_dna_locations_widget.verticalHeader().setVisible(False)
        self.hints_dna_locations_widget.verticalHeader().setMinimumSectionSize(30)
        self.hints_dna_locations_widget.verticalHeader().setDefaultSectionSize(30)
        self.hints_dna_locations_widget.verticalHeader().setProperty("showSortIndicator", False)
        self.hints_dna_locations_widget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_2.addWidget(self.hints_dna_locations_widget)

        self.hints_label_3 = QLabel(self.hints_scroll_area_contents)
        self.hints_label_3.setObjectName(u"hints_label_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.hints_label_3.sizePolicy().hasHeightForWidth())
        self.hints_label_3.setSizePolicy(sizePolicy3)
        self.hints_label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.hints_label_3.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.hints_label_3)

        self.hints_scroll_area.setWidget(self.hints_scroll_area_contents)

        self.gridLayout.addWidget(self.hints_scroll_area, 0, 0, 1, 1)

        SamusReturnsGameTabWidget.addTab(self.hints_tab, "")
        self.hint_item_names_tab = QWidget()
        self.hint_item_names_tab.setObjectName(u"hint_item_names_tab")
        self.hint_item_names_layout = QVBoxLayout(self.hint_item_names_tab)
        self.hint_item_names_layout.setSpacing(0)
        self.hint_item_names_layout.setContentsMargins(11, 11, 11, 11)
        self.hint_item_names_layout.setObjectName(u"hint_item_names_layout")
        self.hint_item_names_layout.setContentsMargins(0, 0, 0, 0)
        self.hint_item_names_scroll_area = QScrollArea(self.hint_item_names_tab)
        self.hint_item_names_scroll_area.setObjectName(u"hint_item_names_scroll_area")
        self.hint_item_names_scroll_area.setWidgetResizable(True)
        self.hint_item_names_scroll_area.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.hint_item_names_scroll_contents = QWidget()
        self.hint_item_names_scroll_contents.setObjectName(u"hint_item_names_scroll_contents")
        self.hint_item_names_scroll_contents.setGeometry(QRect(0, 0, 665, 646))
        self.hint_item_names_scroll_layout = QVBoxLayout(self.hint_item_names_scroll_contents)
        self.hint_item_names_scroll_layout.setSpacing(6)
        self.hint_item_names_scroll_layout.setContentsMargins(11, 11, 11, 11)
        self.hint_item_names_scroll_layout.setObjectName(u"hint_item_names_scroll_layout")
        self.hint_item_names_label = QLabel(self.hint_item_names_scroll_contents)
        self.hint_item_names_label.setObjectName(u"hint_item_names_label")
        self.hint_item_names_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.hint_item_names_label.setWordWrap(True)

        self.hint_item_names_scroll_layout.addWidget(self.hint_item_names_label)

        self.hint_item_names_tree_widget = QTableWidget(self.hint_item_names_scroll_contents)
        if (self.hint_item_names_tree_widget.columnCount() < 4):
            self.hint_item_names_tree_widget.setColumnCount(4)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.hint_item_names_tree_widget.setHorizontalHeaderItem(0, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.hint_item_names_tree_widget.setHorizontalHeaderItem(1, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.hint_item_names_tree_widget.setHorizontalHeaderItem(2, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.hint_item_names_tree_widget.setHorizontalHeaderItem(3, __qtablewidgetitem35)
        self.hint_item_names_tree_widget.setObjectName(u"hint_item_names_tree_widget")
        self.hint_item_names_tree_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.hint_item_names_tree_widget.setSortingEnabled(True)

        self.hint_item_names_scroll_layout.addWidget(self.hint_item_names_tree_widget)

        self.hint_item_names_scroll_area.setWidget(self.hint_item_names_scroll_contents)

        self.hint_item_names_layout.addWidget(self.hint_item_names_scroll_area)

        SamusReturnsGameTabWidget.addTab(self.hint_item_names_tab, "")
        self.hint_locations_tab = QWidget()
        self.hint_locations_tab.setObjectName(u"hint_locations_tab")
        self.hint_tab_layout = QVBoxLayout(self.hint_locations_tab)
        self.hint_tab_layout.setSpacing(6)
        self.hint_tab_layout.setContentsMargins(11, 11, 11, 11)
        self.hint_tab_layout.setObjectName(u"hint_tab_layout")
        self.hint_tab_layout.setContentsMargins(0, 0, 0, 0)
        self.hint_locations_scroll_area = QScrollArea(self.hint_locations_tab)
        self.hint_locations_scroll_area.setObjectName(u"hint_locations_scroll_area")
        self.hint_locations_scroll_area.setWidgetResizable(True)
        self.hint_locations_scroll_area.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.hint_locations_scroll_contents = QWidget()
        self.hint_locations_scroll_contents.setObjectName(u"hint_locations_scroll_contents")
        self.hint_locations_scroll_contents.setGeometry(QRect(0, 0, 665, 646))
        self.hint_scroll_layout = QVBoxLayout(self.hint_locations_scroll_contents)
        self.hint_scroll_layout.setSpacing(6)
        self.hint_scroll_layout.setContentsMargins(11, 11, 11, 11)
        self.hint_scroll_layout.setObjectName(u"hint_scroll_layout")
        self.hint_locations_label = QLabel(self.hint_locations_scroll_contents)
        self.hint_locations_label.setObjectName(u"hint_locations_label")
        self.hint_locations_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.hint_locations_label.setWordWrap(True)

        self.hint_scroll_layout.addWidget(self.hint_locations_label)

        self.hint_locations_tree_widget = QTreeWidget(self.hint_locations_scroll_contents)
        self.hint_locations_tree_widget.setObjectName(u"hint_locations_tree_widget")

        self.hint_scroll_layout.addWidget(self.hint_locations_tree_widget)

        self.hint_locations_scroll_area.setWidget(self.hint_locations_scroll_contents)

        self.hint_tab_layout.addWidget(self.hint_locations_scroll_area)

        SamusReturnsGameTabWidget.addTab(self.hint_locations_tab, "")

        self.retranslateUi(SamusReturnsGameTabWidget)

        SamusReturnsGameTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SamusReturnsGameTabWidget)
    # setupUi

    def retranslateUi(self, SamusReturnsGameTabWidget):
        self.game_cover_label.setText(QCoreApplication.translate("SamusReturnsGameTabWidget", u"TextLabel", None))
        self.intro_label.setText(QCoreApplication.translate("SamusReturnsGameTabWidget", u"<html><head/><body><p>Traverse SR388 while collecting Metroid DNA in order to fight Proteus Ridley and bring the Baby to the Ship.</p><p>Accessing Ridley is blocked unless you have collected enough DNA. You can find them by defeating bosses, Metroids, or anywhere in the world. The default settings require you to collect 10 Metroid DNA placed on Metroids.</p><p>Each Chozo Seal will provide a hint to where an item is by specifiying the region in which is resides. New seals have been added which provides hints to where Metroid DNA is located. Check out the <a href=\"tab://Hints\"><span style=\" text-decoration: underline; color:#007af4;\">Hints</span></a> tab for more information.</p><p>The HUD shows how much DNA is located in each area.</p><p>For more details, check out the <a href=\"tab://FAQ\"><span style=\" text-decoration: underline; color:#007af4;\">FAQ</span></a> and <a href=\"tab://Differences\"><span style=\" text-decoration: underline; color:#007af4;\">Differences</span></a> tabs.</p><p>To get started, "
                        "use the Quick Generate button to generate a game using the default settings!</p></body></html>", None))
        self.quick_generate_button.setText(QCoreApplication.translate("SamusReturnsGameTabWidget", u"Quick generate", None))
        SamusReturnsGameTabWidget.setTabText(SamusReturnsGameTabWidget.indexOf(self.tab_intro), QCoreApplication.translate("SamusReturnsGameTabWidget", u"Introduction", None))
        SamusReturnsGameTabWidget.setTabText(SamusReturnsGameTabWidget.indexOf(self.tab_generate_game), QCoreApplication.translate("SamusReturnsGameTabWidget", u"Play", None))
        self.faq_label.setText(QCoreApplication.translate("SamusReturnsGameTabWidget", u"# updated from code", None))
        SamusReturnsGameTabWidget.setTabText(SamusReturnsGameTabWidget.indexOf(self.faq_tab), QCoreApplication.translate("SamusReturnsGameTabWidget", u"FAQ", None))
        self.differences_label.setText(QCoreApplication.translate("SamusReturnsGameTabWidget", u"<html><head/><body><p>Randovania makes some changes to the original game in order to improve the game experience or to simply fix bugs in the original game.</p><p><br/><span style=\" font-weight:600;\">General Changes</span></p><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Chozo Seals have been repurposed to provide hints for where items are located.</li></ul><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">DNA can now be placed anywhere in the world as pickups.</li><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:"
                        "0px; -qt-block-indent:0; text-indent:0px;\">New DNA Seals have been added in most areas that provide hints for where Metroid DNA is located. See the <a href=\"tab:/Hints\"><span style=\" text-decoration: underline; color:#007af4;\">Hints</span></a> tab for more information.</li></ul><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Baby Metroid can now be shuffled.</li></ul><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The amiibo Reserve Tanks no longer require using amiibo to unlock, and are now shuffleable as pickups.</li><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Proteus Ridley is accessible from Surface - West only after the configurable amount of Metroid DNA has been co"
                        "llected.</li><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Most cutscenes have been removed.</li><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Scan Pulse no longer uses up Aeion (still requires at least 1 Aeion to activate).</li><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Warp to Start has been added. Cancel the save prompt at a Save Station or the Ship to warp back to your starting location.</li></ul><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Collecting a tank refills that ammo type to maximum capacity.</li></ul><p><span style=\" font-weight:600;\">Enemy Changes</span></p><ul style=\"margin-top: "
                        "0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Metroids now can drop any item instead of just DNA.</li></ul><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The fleeing Gamma Metroids no longer flee after taking a certain amount of damage. They also always spawn in the same location rather than being random.</li></ul><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Power Bomb drop chances from enemies has been slightly increased.</li><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0p"
                        "x; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Beams have been rebalanced against Proteus Ridley.</li></ul><p><span style=\" font-weight:600;\">Room Changes</span></p><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The hazardous liquid that prevents leaving areas early has been removed.</li></ul><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">All designated heat rooms are now properly heated.</li></ul><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Digger"
                        "naut Chase sequence has been removed and the corresponding rooms have been set to their post-chase state.</li><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The wall blocking the Landing Site from Surface - East after defeating the Queen has been removed.</li><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In the vanilla game, the Surface area where Proteus Ridley resides is a separate map from the starting Surface. These are normally not connected. This has been changed to warp the player to the other Surface map by passing the Baby blocks in the Landing Site. Once enough DNA is collected to access Ridley, you can no longer warp from Surface West to Surface East.</li></ul><p><span style=\" font-weight:600;\">Door Changes</span></p><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:"
                        "12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Most Charge Beam doors at the entrance and exit of every area have been changed to Power Beam doors, excluding Area 4 - Crystal Mines and Area 6.</li><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Most beam doors are now double-sided. This simplifies traversing through areas in reverse.</li><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Some one-way doors are now two-way to prevent softlocks or make traversal less restrictive. These include: <br/><br/><span style=\" font-weight:600;\">Area 1</span><br/></li></ul><ul type=\"circle\" style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\"><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Bomb Chamb"
                        "er to Bomb Chamber Access</li><ul type=\"circle\" style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\"><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Temple Exterior to Inner Temple East Hall </li></ul><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Exterior Alpha Arena to Temple Exterior</li><p><span style=\" font-weight:600;\">Area 3</span></p><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The one-way doors in Transport to Area 2 and Transport to Area 4</li><p><span style=\" font-weight:600;\">Area 4</span></p><ul type=\"circle\" style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\"><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-"
                        "indent:0px;\">Caves Intersection Terminal to Transport to Area 3 and Crystal Mines</li></ul><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Mines Intersection Terminal to Super Missile Chamber</li><p><span style=\" font-weight:600;\">Area 5</span></p><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Plasma Beam Chamber to Grapple Shuffler and Autrack Acropolis</li><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Gravity Suit Chamber to Gravity Suit Chamber Access</li></ul></body></html>", None))
        SamusReturnsGameTabWidget.setTabText(SamusReturnsGameTabWidget.indexOf(self.differences_tab), QCoreApplication.translate("SamusReturnsGameTabWidget", u"Differences", None))
        self.hints_label.setText(QCoreApplication.translate("SamusReturnsGameTabWidget", u"<html><head/><body><p>In Metroid: Samus Returns, you can find hints by using <span style=\" font-weight:600;\">Chozo Seals</span>.</p><p align=\"justify\">Seals found at the start of each area found in the vanilla game each provide one hint to where an item is located.</p></body></html>", None))
        self.hints_label_2.setText(QCoreApplication.translate("SamusReturnsGameTabWidget", u"<html><head/><body><p>Custom Chozo Seals have also been added to some areas which provide hints to Metroid DNA. Each seal provides a random number of hints which sometimes is no hints. In this case, a joke hint is provided instead. These custom seals can be found in the following areas:</p></body></html>", None))
        ___qtablewidgetitem = self.hints_dna_locations_widget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("SamusReturnsGameTabWidget", u"Location", None));
        ___qtablewidgetitem1 = self.hints_dna_locations_widget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("SamusReturnsGameTabWidget", u"Maximum amount of DNA hints", None));
        ___qtablewidgetitem2 = self.hints_dna_locations_widget.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("SamusReturnsGameTabWidget", u"New Row", None));
        ___qtablewidgetitem3 = self.hints_dna_locations_widget.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("SamusReturnsGameTabWidget", u"New Row", None));
        ___qtablewidgetitem4 = self.hints_dna_locations_widget.verticalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("SamusReturnsGameTabWidget", u"New Row", None));
        ___qtablewidgetitem5 = self.hints_dna_locations_widget.verticalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("SamusReturnsGameTabWidget", u"New Row", None));
        ___qtablewidgetitem6 = self.hints_dna_locations_widget.verticalHeaderItem(4)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("SamusReturnsGameTabWidget", u"New Row", None));
        ___qtablewidgetitem7 = self.hints_dna_locations_widget.verticalHeaderItem(5)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("SamusReturnsGameTabWidget", u"New Row", None));
        ___qtablewidgetitem8 = self.hints_dna_locations_widget.verticalHeaderItem(6)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("SamusReturnsGameTabWidget", u"New Row", None));
        ___qtablewidgetitem9 = self.hints_dna_locations_widget.verticalHeaderItem(7)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("SamusReturnsGameTabWidget", u"New Row", None));
        ___qtablewidgetitem10 = self.hints_dna_locations_widget.verticalHeaderItem(8)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("SamusReturnsGameTabWidget", u"New Row", None));
        ___qtablewidgetitem11 = self.hints_dna_locations_widget.verticalHeaderItem(9)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("SamusReturnsGameTabWidget", u"New Row", None));

        __sortingEnabled = self.hints_dna_locations_widget.isSortingEnabled()
        self.hints_dna_locations_widget.setSortingEnabled(False)
        ___qtablewidgetitem12 = self.hints_dna_locations_widget.item(0, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("SamusReturnsGameTabWidget", u"Surface: West - Transport to Area 8", None));
        ___qtablewidgetitem13 = self.hints_dna_locations_widget.item(0, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("SamusReturnsGameTabWidget", u"1", None));
        ___qtablewidgetitem14 = self.hints_dna_locations_widget.item(1, 0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("SamusReturnsGameTabWidget", u"Area 1 - Metroid Caverns Lobby", None));
        ___qtablewidgetitem15 = self.hints_dna_locations_widget.item(1, 1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("SamusReturnsGameTabWidget", u"4", None));
        ___qtablewidgetitem16 = self.hints_dna_locations_widget.item(2, 0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("SamusReturnsGameTabWidget", u"Area 2: Dam Exterior - Metroid Caverns Teleporter", None));
        ___qtablewidgetitem17 = self.hints_dna_locations_widget.item(2, 1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("SamusReturnsGameTabWidget", u"5", None));
        ___qtablewidgetitem18 = self.hints_dna_locations_widget.item(3, 0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("SamusReturnsGameTabWidget", u"Area 3: Metroid Caverns - Gamma+ Arena South", None));
        ___qtablewidgetitem19 = self.hints_dna_locations_widget.item(3, 1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("SamusReturnsGameTabWidget", u"6", None));
        ___qtablewidgetitem20 = self.hints_dna_locations_widget.item(4, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("SamusReturnsGameTabWidget", u"Area 4: Crystal Mines - Basalt Basin", None));
        ___qtablewidgetitem21 = self.hints_dna_locations_widget.item(4, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("SamusReturnsGameTabWidget", u"4", None));
        ___qtablewidgetitem22 = self.hints_dna_locations_widget.item(5, 0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("SamusReturnsGameTabWidget", u"Area 5: Tower Exterior - Tower Exterior", None));
        ___qtablewidgetitem23 = self.hints_dna_locations_widget.item(5, 1)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("SamusReturnsGameTabWidget", u"5", None));
        ___qtablewidgetitem24 = self.hints_dna_locations_widget.item(6, 0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("SamusReturnsGameTabWidget", u"Area 6 - Hideout Sprawl", None));
        ___qtablewidgetitem25 = self.hints_dna_locations_widget.item(6, 1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("SamusReturnsGameTabWidget", u"3", None));
        ___qtablewidgetitem26 = self.hints_dna_locations_widget.item(7, 0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("SamusReturnsGameTabWidget", u"Area 6 - Crumbling Stairwell", None));
        ___qtablewidgetitem27 = self.hints_dna_locations_widget.item(7, 1)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("SamusReturnsGameTabWidget", u"3", None));
        ___qtablewidgetitem28 = self.hints_dna_locations_widget.item(8, 0)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("SamusReturnsGameTabWidget", u"Area 7 - Wallfire Workstation", None));
        ___qtablewidgetitem29 = self.hints_dna_locations_widget.item(8, 1)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("SamusReturnsGameTabWidget", u"3", None));
        ___qtablewidgetitem30 = self.hints_dna_locations_widget.item(9, 0)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("SamusReturnsGameTabWidget", u"Area 8 - Hatchling Room*", None));
        ___qtablewidgetitem31 = self.hints_dna_locations_widget.item(9, 1)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("SamusReturnsGameTabWidget", u"5", None));
        self.hints_dna_locations_widget.setSortingEnabled(__sortingEnabled)

        self.hints_label_3.setText(QCoreApplication.translate("SamusReturnsGameTabWidget", u"<html><head/><body><p>*The DNA Seal in Area 8 - Hatchling Room is inactive until <span style=\" font-style:italic;\">after</span> the Metroid Queen has been defeated.</p></body></html>", None))
        SamusReturnsGameTabWidget.setTabText(SamusReturnsGameTabWidget.indexOf(self.hints_tab), QCoreApplication.translate("SamusReturnsGameTabWidget", u"Hints", None))
        self.hint_item_names_label.setText(QCoreApplication.translate("SamusReturnsGameTabWidget", u"<html><head/><body><p>When items are referenced in a hint, multiple names can be used depending on how precise the hint is. These additional names are not used by hints in Metroid: Samus Returns, but can be used if hinted by another game such as Metroid Prime 2: Echoes.</p><p>The names each item can use are the following: </p></body></html>", None))
        ___qtablewidgetitem32 = self.hint_item_names_tree_widget.horizontalHeaderItem(0)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("SamusReturnsGameTabWidget", u"Item", None));
        ___qtablewidgetitem33 = self.hint_item_names_tree_widget.horizontalHeaderItem(1)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("SamusReturnsGameTabWidget", u"Precise Category", None));
        ___qtablewidgetitem34 = self.hint_item_names_tree_widget.horizontalHeaderItem(2)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("SamusReturnsGameTabWidget", u"General Category", None));
        ___qtablewidgetitem35 = self.hint_item_names_tree_widget.horizontalHeaderItem(3)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("SamusReturnsGameTabWidget", u"Broad Category", None));
        SamusReturnsGameTabWidget.setTabText(SamusReturnsGameTabWidget.indexOf(self.hint_item_names_tab), QCoreApplication.translate("SamusReturnsGameTabWidget", u"Hint Item Names", None))
        self.hint_locations_label.setText(QCoreApplication.translate("SamusReturnsGameTabWidget", u"<html><head/><body><p>Hints\n"
"                                                are placed in the game by replacing Logbook scans. The\n"
"                                                following are the scans that may have a hint added to\n"
"                                                them:</p></body></html>\n"
"                                            ", None))
        ___qtreewidgetitem = self.hint_locations_tree_widget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("SamusReturnsGameTabWidget", u"Location", None));
        SamusReturnsGameTabWidget.setTabText(SamusReturnsGameTabWidget.indexOf(self.hint_locations_tab), QCoreApplication.translate("SamusReturnsGameTabWidget", u"Hints Locations", None))
        pass
    # retranslateUi

