"""
This File contains stylesheet themes for the Application
"""

TITLE_STYLE = """
    color: #000111;
    font-size: 30px;
    font-weight: semibold;

"""
BODY_STYLE = """
    color: #111111;
    font-size: 16px;
"""

ADD_BTN_STYLE = """
QPushButton {
    background    : #2383E2;
    color         : #FFF;
    border        : none;
    border-radius : 6px;
    font-size     : 16px;
    font-weight   : semibold;
    font-family   : 'Segoe UI', sans-serif;
    padding       : 7px 20px;
}
QPushButton:hover   { background: #1A73CE; }
QPushButton:pressed { background: #1260B5; }
"""

TAB_WIDG_STYLE = """            

QTabBar {
    background      : transparent;
    border-bottom   : 1px solid #cdcdcd;
}

QTabBar::tab {
    background      : transparent;
    color           : #6B6B69;
    border          : 1px solid transparent;
    border-radius   : 6px;
    font-size       : 12.5px;
    font-family     : 'Segoe UI', sans-serif;
    padding         : 4px 14px;
    margin          : 8px 2px;
    min-height      : 30px;
}

QTabBar::tab:hover {
    background      : #F0EFED;
    color           : #1C1C1C;
}

QTabBar::tab:selected {
    background      : #E8F3FE;
    color           : #2383E2;
    border          : 1px solid #B4D1F8;
    font-weight     : 600;
}
"""