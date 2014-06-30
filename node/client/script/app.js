function init() {
    socket = io.connect('http://localhost:3000');

    socket.on('my_event',function(type){
        console.log('Event');
    });
    console.log('Initialized');
}
