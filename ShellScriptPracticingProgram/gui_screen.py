# Side bar gui screen

import os
import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QFileSystemModel, QTreeView, QApplication

class GUIScreen(QWidget) :
    def __init__(self, user_name) :
        super().__init__()
        self.user_name = user_name
        layout = QVBoxLayout()

        self.tree = QTreeView()
        self.model = QFileSystemModel()

        # 현재 스크립트 기준으로 vroot 경로 설정
        base_dir = os.path.dirname(os.path.abspath(__file__))  
        root_path = os.path.join(base_dir, f"vroot_{self.user_name}")    

        # vroot 디렉토리가 없으면 오류 방지를 위해 생성
        if not os.path.exists(root_path) :
            os.makedirs(root_path)

        self.model.setRootPath(root_path)
        self.tree.setModel(self.model)

        # 트리뷰 설정
        root_index = self.model.index(root_path)
        self.tree.setRootIndex(root_index)

        self.tree.setRootIsDecorated(True)
        self.tree.setHeaderHidden(False)
        self.tree.setAnimated(True)
        self.tree.setIndentation(20)
        self.tree.setSortingEnabled(True)

        layout.addWidget(QLabel(f"File Viewer (User : vroot_{self.user_name}/)"))
        layout.addWidget(self.tree)
        self.setLayout(layout)

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = GUIScreen()
    window.show()
    sys.exit(app.exec_())
