// const socket = new WebSocket("ws://192.168.3.127:8000/ws/front/");//"ws://127.0.0.1:8000/ws/front/"
const socket = new WebSocket("ws://192.168.0.198:8000/ws/front/");//"ws://127.0.0.1:8000/ws/front/"
  socket.addEventListener("open", function (event) {
    socket.send(
      JSON.stringify({
        message: "datos",      
      })
    );
  });
  
  // Escucha cierre de WebSocket
  socket.onclose = function (event) {
      window.location.reload();
    };

    window.addEventListener("hashchange", () => {                  //cuando tocas f5
      (window.location.hash);
  });

  window.addEventListener("DOMContentLoaded", () => {                         //todo el tiempo
    (window.location.hash);
    //MENSAJES
    cuadroDeTextoIndex = document.querySelector("#terminalDeTexto");
    // if (sessionStorage.getItem("vf4_msg") && cuadroDeTextoIndex) {
    //     let ul = document.getElementById("cuadroMensajes");
    //     const listaMensajes = sessionStorage.getItem("vf4_msg").split(",").reverse();
    //     for (let i = 0; i < listaMensajes.length; i++) {
    //         const li = document.createElement("li");
    //         li.setAttribute("style", "list-style: none;");
    //         li.innerHTML = listaMensajes[i];
    //         ul.appendChild(li);
    //     }
    // }
    // console.log("Enter main js");
  });


  socket.onmessage = function (event) {
    // var start = Date.now();
    const datosWs = JSON.parse(event.data);
    // console.log(datosWs);

    switch (window.location.pathname) {
      case "/timer/":
        timer(datosWs)
        break
    }
    
  };