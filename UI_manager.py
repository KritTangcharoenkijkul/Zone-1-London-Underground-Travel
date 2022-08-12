import sys
import time

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

from UI_start_page import *
from UI_result_page import *
from UI_routing_page import *

from NextStation_Controller import *


class UI_Manager(QMainWindow):

    def __init__(self, parent = None):
        #init attribute
        self.time = "null"
        
        QMainWindow.__init__(self, None) #init

        #set up main UI
        self.setMinimumSize(1160,1000)
        self.setMaximumSize(1160,1000)
        self.parent = parent
        self.setWindowTitle("NextStation")
        
        QApplication.setStyle(QStyleFactory.create("Plastique"))
        
        #add background img
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("UIDesign/UIBackground/StartPageUI.png")))
        self.setPalette(palette)
        

        #create stackedwidget + show first page
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
        start_page_widget = StartPage(self)
        self.central_widget.addWidget(start_page_widget)


        #add widget
        self.start_page = StartPage(self)
        self.routing_page = RoutingPage(self)
        self.result_page = PathResultPage(self)
            
        #set central widget
        self.central_widget.addWidget(self.start_page)
        self.central_widget.addWidget(self.routing_page)
        self.central_widget.addWidget(self.result_page)

        #create page library
        self.page_list = [self.start_page, self.routing_page, self.result_page]
        self.page_background = [QPixmap("UIDesign/UIBackground/StartPageUI.png"),
                                QPixmap("UIDesign/UIBackground/RoutePageUI2.png"),
                                QPixmap("UIDesign/UIBackground/ResultPageUI.png")]


    def user_request(self, request):
        if(request[0] == "astar_time"): # request["astar_time",from,to]
            if(self.time == "null"):
                day = time.strftime("%a") 
                hour, mins = time.strftime("%H:%M").split(':')
                self.time = [day,hour,mins]
                
            result = getShortestPath(request[1],request[2],self.time) # path, cost, train, row, col, exit, place
         
            
            #change page
            self.routing_page.clear()
            self.result_page.updateGUI(result)
            self.changePage(2)

        if(request[0] == "place_details"): # request["place_details", place_name]
            result = getPlaceDetails(request[1])

            return result
            
        
    def changePage(self, page):

        #change page's background
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(self.page_background[page]))
        self.setPalette(palette)

        self.start_page.updateGUI()
        self.centralWidget().setCurrentWidget(self.page_list[page]) 


    def clearLayout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
            elif child.layout() is not None:
                self.clearLayout(child.layout())
                
    def getColor(self, train):
        if (train == "bak"):
            return "QPushButton{border-image:url(" + "UIDesign/StationIcon/baker0.png" + ") }QPushButton:hover{border-image:url(" + "UIDesign/StationIcon/baker1.png" + ") }"
        elif (train == "ham"):
            return "QPushButton{border-image:url(" + "UIDesign/StationIcon/hammer0.png" + ") }QPushButton:hover{border-image:url(" + "UIDesign/StationIcon/hammer1.png" + ") }"
        elif (train == "met"):
            return "QPushButton{border-image:url(" + "UIDesign/StationIcon/metro0.png" + ") }QPushButton:hover{border-image:url(" + "UIDesign/StationIcon/metro1.png" + ") }"
        elif (train == "cen"):
            return "QPushButton{border-image:url(" + "UIDesign/StationIcon/central0.png" + ") }QPushButton:hover{border-image:url(" + "UIDesign/StationIcon/central1.png" + ") }"
        elif (train == "pic"):
            return "QPushButton{border-image:url(" + "UIDesign/StationIcon/pic0.png" + ") }QPushButton:hover{border-image:url(" + "UIDesign/StationIcon/pic1.png" + ") }"
        elif (train == "dis"):
            return "QPushButton{border-image:url(" + "UIDesign/StationIcon/district0.png" + ") }QPushButton:hover{border-image:url(" + "UIDesign/StationIcon/district1.png" + ") }"
        elif (train == "cir"):
            return "QPushButton{border-image:url(" + "UIDesign/StationIcon/circle0.png" + ") }QPushButton:hover{border-image:url(" + "UIDesign/StationIcon/circle1.png" + ") }"
        elif (train == "jub"):
            return "QPushButton{border-image:url(" + "UIDesign/StationIcon/j0.png" + ") }QPushButton:hover{border-image:url(" + "UIDesign/StationIcon/j1.png" + ") }"
        elif (train == "vic"):
            return "QPushButton{border-image:url(" + "UIDesign/StationIcon/victoria0.png" + ") }QPushButton:hover{border-image:url(" + "UIDesign/StationIcon/victoria1.png" + ") }"
        elif (train == "nor"):
            return "QPushButton{border-image:url(" + "UIDesign/StationIcon/north0.png" + ") }QPushButton:hover{border-image:url(" + "UIDesign/StationIcon/north1.png" + ") }"
        else:
            return "pink"
        


def main():
        app = QApplication(sys.argv)

        w = UI_Manager()
        w.show()
        return app.exec_()

if __name__ == "__main__":
        sys.exit(main())
