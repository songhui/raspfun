var clientFromConnectionString = require('azure-iot-device-mqtt').clientFromConnectionString;
var Message = require('azure-iot-device').Message;
 
var connectionString = 'HostName=EnactHubStandard.azure-devices.net;DeviceId=TelluSimu02;SharedAccessKey=E5Sl7QVhbyXL9dzRok/v21MKSDHU6cFRJkf+d5BwXDc=';
 
var client = clientFromConnectionString(connectionString);

var sendMessage = ()=>{
    var data = JSON.stringify({button: "on"});
    var message = new Message(data);
    client.sendEvent(message, function (err) {
        if (err) console.log(err.toString());
    });
    console.log('sent '+ data)
    setTimeout(sendMessage, 10000)
}

var connectCallback = function (err) {
    if (err) {
      console.error('Could not connect: ' + err);
    } else {
      console.log('Client connected');
      sendMessage()
    }
  };

  client.open(connectCallback);