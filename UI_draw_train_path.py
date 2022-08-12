from PySide.QtCore import *
from PySide.QtGui import *



class DrawTrainPath(QWidget):
    def __init__(self, data_list, parent=None):
        QWidget.__init__(self, parent)
        # setGeometry(x_pos, y_pos, width, height)
        #self.setStyleSheet("QWidget{background-color: \"#F3F3F3\";}")
        self.data_list = data_list
        self.setGeometry(100, 100, 1150, 570)

        if(self.data_list[2][0] == "walk"):
           self.data_list[2].pop(0)
           self.data_list[0].pop(0)

                   
        if(self.data_list[3] == "2" or self.data_list[3] == "3"):
            y = 114
        elif(self.data_list[3] == "4" or self.data_list[3] == "5"):
            y = 57
        else:
            y = 228
            
        x1 = 125
        y1 = y
        x2 = 125
        y2 = y

        ## data structure
        self.station_name_list = [[self.data_list[0][0],x1,y1]]
        self.name_count = 0
        
        self.line_list = []
        self.grey_line_list = []
        self.circle_list = []
        self.small_circle_list =[]

        self.legend = ["Bakerloo Line", "Hammersmith & City Line", "Metropolitan Line", "Central Line", "Piccadilly Line", "District Line", "Circle Line", "Jubilee Line", "Victoria Line", "Northern Line"]
        self.legend_color = [QColor("#b05f0f"),QColor("#f386a0"),QColor("#97015e"),QColor("#ee2e22"),QColor("#1b3f94"),QColor("#00843d"),QColor("#fed105"),QColor("#959ca1"),QColor("#069ddc"),QColor("#231f20")]
        
        deltaX = 900.00/(int(self.data_list[4]) + 1)

        self.line_color_list = []
        self.circle_color_list = []
        
        previous_color = "#ffffff"

        sequence_list = self.getColorSequence()
        index = 0
        # generate line
        for i in range(len(data_list[2]) - 1):
            if(data_list[2][i] != "walk"):
                x2 += deltaX
                self.line_list.append([x1,y1,x2,y2])
                self.circle_list.append([x1 - 12.5,y1 - 12.5,25,25])
                self.small_circle_list.append([x1 - 4.5, y1 - 4.5,9,9])

                self.line_color_list.append(self.getColor(sequence_list[index]))
                previous_color = self.getColor(self.data_list[2][i])
                self.circle_color_list.append(previous_color)

                
            else:
                
                self.station_name_list.append([self.data_list[0][self.name_count],x1,y1])
                
                self.circle_list.append([x1 - 12.5,y1 - 12.5, 25,25])
                self.small_circle_list.append([x1 - 4.5, y1 - 4.5,9,9])
                y1 += 114
                self.grey_line_list.append([x1,y1,x2,y2])
                y2 += 114

                index += 1
                self.circle_color_list.append(previous_color)

            self.name_count += 1
    
            x1 = x2

        self.circle_list.append([x1 - 6.25,y1 - 12.5, 25,25])
        self.circle_color_list.append(previous_color)

        #self.name_count += 1
        self.station_name_list.append([self.data_list[0][len(self.data_list[0])-1],x1,y1])


    def paintEvent(self, event):
        paint = QPainter()
        paint.begin(self)
        
        paint.setRenderHint(QPainter.Antialiasing)
        
        paint.setPen(QPen(QColor("#F3F3F3"),20,Qt.SolidLine))
        paint.setBrush(QColor('#FFFFFF'))
        paint.drawRect(event.rect())

        for i in range(len(self.grey_line_list)):
            paint.setPen(QPen(QColor("#D7D8DA"),10,Qt.SolidLine))
            paint.drawLine(self.grey_line_list[i][0],self.grey_line_list[i][1],self.grey_line_list[i][2],self.grey_line_list[i][3])
            
        for i in range(len(self.line_list)):
            paint.setPen(QPen(QColor(self.line_color_list[i]),20,Qt.SolidLine))
            paint.drawLine(self.line_list[i][0],self.line_list[i][1],self.line_list[i][2],self.line_list[i][3])
        
        for i in range(len(self.circle_list)):
            paint.setPen(QPen(QColor(self.circle_color_list[i]),20,Qt.SolidLine))
            paint.drawArc(self.circle_list[i][0],self.circle_list[i][1],self.circle_list[i][2],self.circle_list[i][3],0,16*360)
            

        #for i in range(len(self.small_circle_list)):
        #    paint.setPen(QPen(QColor("white"),20,Qt.SolidLine))
        #    paint.drawArc(self.small_circle_list[i][0],self.small_circle_list[i][1],self.small_circle_list[i][2],self.small_circle_list[i][3],0,16*360)

        #paint.setPen(QPen(QColor(self.circle_color_list[0]),20,Qt.SolidLine))
        #paint.drawArc(self.circle_list[0][0],self.circle_list[0][1],self.circle_list[0][2],self.circle_list[0][3],0,16*360)

        paint.setPen(QPen(QColor("white"),20,Qt.SolidLine))
        paint.drawArc(self.small_circle_list[0][0],self.small_circle_list[0][1],self.small_circle_list[0][2],self.small_circle_list[0][3],0,16*360)

        paint.setPen(QPen(QColor("white"),20,Qt.SolidLine))
        paint.drawArc(self.circle_list[len(self.circle_list)-1][0] + 8 ,self.circle_list[len(self.circle_list)-1][1] + 6.5,9,9,0,16*360)    


        paint.setPen(QPen(QColor("#F3F3F3"),5,Qt.SolidLine))
        paint.drawRect(40, 365, 300, 170)

        # draw legend
        for i in range(len(self.legend)):
            paint.setPen(QPen(self.legend_color[i],5,Qt.SolidLine))
            #paint.drawRect(55, 380 + i * 30, 20,20)
            paint.fillRect(55, 380 + i * 30, 20,20, self.legend_color[i])

            font = paint.font()
            font.setPointSize(10)
            paint.setFont(font)

            paint.drawText(75, 400 + i * 30, "   " + self.legend[i])
            
        for i in range(len(self.station_name_list)):
            paint.setPen(QPen(QColor(0,0,0),5,Qt.SolidLine))
            paint.drawText(self.station_name_list[i][1], self.station_name_list[i][2] - 35, " " + self.station_name_list[i][0])

        
    def getColor(self, train):
        if(train == "Bakerloo Line"):
            return "#b05f0f"
        elif(train == "Hammersmith & City Line"):
            return "#f386a0"
        elif(train == "Metropolitan Line"):
            return "#97015e"
        elif(train == "Central Line"):
            return "#ee2e22"
        elif(train == "Piccadilly Line"):
            return "#1b3f94"
        elif(train == "District Line"):
            return "#00843d"
        elif(train == "Circle Line"):
            return "#fed105"
        elif(train == "Jubilee Line"):
            return "#959ca1"
        elif(train == "Victoria Line"):
            return "#069ddc"
        elif(train == "Northern Line"):
            return "#231f20"
        
    def getColorSequence(self):
        sequence_list = []
        for i in range(len(self.data_list[2])):
            if((self.data_list[2][i] not in sequence_list) and
              (self.data_list[2][i] != "walk")):
               sequence_list.append(self.data_list[2][i])


        return sequence_list
