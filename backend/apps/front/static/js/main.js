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
    const btn_end_cicle = document.getElementById("btn_end_cicle")
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
    btn_end_cicle.addEventListener("click", (event) => {
      switch (window.location.pathname) {
        case "/vf4/":
          finishCicle("vf4")
          break
        case "/vf2/":
          finishCicle("vf2")
          break
      }
    });

    function finishCicle(machine){
      let url = "http://192.168.0.198:8000/control/finishCicle/";
      let params = "&machine=" + machine;
      console.log('send command');
  
      // var params = "lorem=ipsum&name=alpha";
      let xhr = new XMLHttpRequest();
      xhr.open("POST", url, true);

      //Send the proper header information along with the request
      xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

      xhr.send(params);
  }
  });


  socket.onmessage = function (event) {
    // var start = Date.now();
    const datosWs = JSON.parse(event.data);
    // console.log(datosWs);

    switch (window.location.pathname) {
      case "/vf4/":
        timer(datosWs)
        break
      case "/vf2/":
        vf2(datosWs)
        break
      case "/st35/":
        st35(datosWs)
        break
    }
    
  };