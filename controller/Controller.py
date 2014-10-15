from devices.Time import *

class Controller:
  
    def __init__(self):
        self.startRecord = -1
        self.endRecord = -1
        self.timer = Time()

    def things2control(self,digital27,arrowLeft):
	self.digital27 = digital27
	self.arrowLeft = arrowLeft	

    def f2(self,channel):
    	self.arrowLeft.setFill(self.digital27.getValue())
    
    def updateAll(self,canvas,mcp3208,serial,controller,rpm,speed,oilTemp,oilPressure,h2o,h2oEcu,battery,fuel,throttle,clutch,brake,runTime,inj,duty,vtec,iat,ign,mapp,arrowLeft,arrowRight,accelerometer,g):

	#rpm.setRpm(serial.getRpm())
        speed.setText(120)#serial.getVss())
        oilTemp.setValue(mcp3208.getADC(7)) 
        oilPressure.setValue(5000)#mcp3208.getADC(6))
        fuel.setWidth(mcp3208.getADC(7))
        h2o.setValue(5000)#mcp3208.getADC(5))
        h2oEcu.setText(int(serial.getEct()))
        battery.setText("12.5")#round(serial.getBattery(),1))
        #throttle.setHeight(mcp3208.getADC(8))
        #clutch.setHeight(mcp3208.getADC(4))
        brake.setHeight(mcp3208.getADC(7))
        time = self.timer.getTime()
        runTime.setText(self.timer.getTimeString())
	axes = accelerometer.getAxes(True)
	g.setGforce(axes['x'],axes['y'])

        canvas.after(10,controller.updateAll,canvas,mcp3208,serial,controller,rpm,speed,oilTemp,oilPressure,h2o,h2oEcu,battery,fuel,throttle,clutch,brake,runTime,inj,duty,vtec,iat,ign,mapp,arrowLeft,arrowRight,accelerometer,g)

    def checkSpeedRecord(self,speed):
        now = self.timer.getTime()
        if speed <= 0:
            self.startRecord=self.timer.getTime()
        elif (speed >= 100) and (now - self.startRecord < self.endRecord - self.startRecord):
            self.endRecord=now
        