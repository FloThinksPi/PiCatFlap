
var express = require('express');
var app = express();
var path    = require('path');

app.use(express.static(path.join(__dirname, 'client')));

var server = app.listen(80, function() {
    console.log('Listening on port %d', server.address().port);
});

var io = require('socket.io').listen(server); 


  //Python 
  var PythonShell = require('python-shell');
  var servo
  //START SERVO-------------------------------
  function newServo(){
    var options = {
     mode: 'text',
     scriptPath: '/home/pi/PiCatFlap/node/PiCode',
     };

    servo = new PythonShell('servo.py',options);

    servo.on('message', function (message) {
     console.log("ServoSystem: "+ message);

     if(message=="ServoClosed"){
        newServo();
     }

     if(message=="ready"){
      io.sockets.emit('updatebutton', "0");
      buttonposition=0;
     }

    });
  }
  newServo();
  //END SERVO

  //START DIMMER-------------------------------
  var options = {
    mode: 'text',
    scriptPath: '/home/pi/PiCatFlap/node/PiCode'
  };
  var CurrentDimmInstance = new PythonShell('dimm.py',options);
  CurrentDimmInstance.send('0');

  CurrentDimmInstance.on('message', function (message) {
    console.log("DimmerS: "+ message);
  });

  //END DIMMER---------------------------------


  //START NOTIFICATION

  var options = {
    mode: 'text',
    scriptPath: '/home/pi/PiCatFlap/node/PiCode'
  };
  var Notify = new PythonShell('notify.py',options);


  Notify.on('message', function (message) {
    console.log("NotifySystem: "+ message);
  });

  //END NOTIFICATION

  function SentToDimmer(data){
    if(Math.round(sliderposition/10)!=Math.round(data/10)){
      CurrentDimmInstance.send(data);
    }
  }

  function SentToServo(data){
    servo.send(data);
  }

  var sliderposition=0;
  var buttonposition=0;
  var TimeOpen=60;

io.sockets.on('connection', function (socket){

  var startdata={
    slider:sliderposition,
    button:buttonposition
  }
	socket.emit('connected',startdata);

  socket.on('sliderchanged', function (data){
  	SentToDimmer(data);
    sliderposition=data;
  	console.log("Dimm At: "+ data/10 + "%");
  	socket.broadcast.emit('updateslider', data);
  });
  

  socket.on('buttonchanged', function (data){
    if(data==1)
    {
      SentToServo(TimeOpen);
    }
    buttonposition=data;
    socket.emit('updatebutton', data);
  	socket.broadcast.emit('updatebutton', data);
  });
  

  socket.on('disconnect', function (){

  });
 
});