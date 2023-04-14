window.addEventListener("DOMContentLoaded", () => {
    (window.location.hash);
        btn_reset = document.getElementById("btn_reset")
        btn_pause = document.getElementById("btn_pause")
        btn_start = document.getElementById("btn_start")
        btn_select = document.getElementById("btn_select")
        btn_finish = document.getElementById("btn_finish")
        btn_add = document.getElementById("btn_add")
        btn_ss_send = document.getElementById("btn_ss_send")
        btn_reset_all = document.getElementById("btn_reset_all")
        input_tiempo_estimado = document.getElementById("tiempo_estimado")
        input_codigo_pieza = document.getElementById("codigo_pieza")
        input_pause_motive = document.getElementById("pause_motive")
        horas = 0
        minutos = 0
        segundos = 0
        horas_stoped = 0
        minutos_stoped = 0
        segundos_stoped = 0
        start_hour = 0
        first_start = 0

    
        
        btn_start.addEventListener("click", (e) => {
            sendCommandTimervf2("start","vf2")
            document.getElementById("pause_state").style.backgroundColor  = '#31af03'
            first_start ++
            if (first_start == 1){
                var today = new Date();
                start_hour = today.toLocaleString();
                sessionStorage.setItem("vf2_startTime", (start_hour));
            }
    
        });
    
        btn_pause.addEventListener("click", (e) => {
            sendCommandTimervf2("pause","vf2")
            btn_start.disabled = true;
            document.getElementById("pause_state").style.backgroundColor  = '#ff0000'
            input_pause_motive.disabled = false;

        });

        btn_reset_all.addEventListener("click", (e) => {
            input_codigo_pieza.disabled = false;
            sendFinishStartPiecevf2("reset_all","vf2")
            first_start = 0
        });

        btn_ss_send.addEventListener("click", (e) => {
            sendSS("vf2")
            input_codigo_pieza.disabled = false;
            input_codigo_pieza.value = 0
        });
    
        btn_reset.addEventListener("click", (e) => {
            input_codigo_pieza.disabled = false;
            sendFinishStartPiecevf2("reset","vf2")
            first_start = 0
            btn_start.disabled = false;

        });

        btn_select.addEventListener("click", (event) => {
            input_codigo_pieza.disabled = true;
            sendFinishStartPiecevf2(true,"vf2")
            sendSelectedPiece(input_codigo_pieza.value,"vf2")
            

        });

        btn_add.addEventListener("click", (e) => {
            if (input_pause_motive.value == "") {
                alert("Campo de errores vacio !")
            } else{
                try {
                    if (!sessionStorage.getItem("vf2_msg_pause")) throw sessionStorage.setItem("vf2_msg_pause", "");
                }
                finally {
                    //poner funcion que empuje todo el mensaje al local en vez de lo q esta bajo
                    sessionStorage.setItem("vf2_msg_pause", JSON.stringify(msg_pause()));
                    value = JSON.parse(sessionStorage.getItem("vf2_msg_pause"))
                    InsertarTexto(value, false)
                    // value_of_pause = (value[1].split(":")).pop() //posicion de vector donde se encuentra el valor del input
                    sendMsgStop(input_pause_motive.value,"vf2")
                    input_pause_motive.value = ""
                    btn_start.disabled = false;
                    input_pause_motive.disabled = true;
                }
            }
        });

        btn_finish.addEventListener("click", (event) => {
            first_start = 0
            sendFinishStartPiecevf2(false,"vf2")
            try {
                if (!sessionStorage.getItem("vf2_msg")) throw sessionStorage.setItem("vf2_msg", "");
            }
            finally {
                //poner funcion que empuje todo el mensaje al local en vez de lo q esta bajo
                sessionStorage.setItem("vf2_msg", JSON.stringify(msg_summary()));
                InsertarTexto(JSON.parse(sessionStorage.getItem("vf2_msg")),true)
                sendFinishStartPiecevf2("reset","vf2")
                document.getElementById("pause_state").style.backgroundColor  = '#0c9df1'
                // sessionStorage.setItem("vf2_msg_pause", "");
                sendMsg(msg_summary(),"vf2")
                sendSelectedPiece("","vf2")

            }
        });


        function sendSS(machine){
            let url = "http://192.168.0.198:8000/control/send_ss/";
            let params = "&machine=" + machine;
            console.log('send command');
        
            // var params = "lorem=ipsum&name=alpha";
            let xhr = new XMLHttpRequest();
            xhr.open("POST", url, true);

            //Send the proper header information along with the request
            xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

            xhr.send(params);
        }


        function sendMsg(common_msg, machine){
            let url = "http://192.168.0.198:8000/control/msg_ss/";
            let params = "&common_msg=" + common_msg + "&machine=" + machine;
            console.log('send command');
        
            // var params = "lorem=ipsum&name=alpha";
            let xhr = new XMLHttpRequest();
            xhr.open("POST", url, true);

            //Send the proper header information along with the request
            xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

            xhr.send(params);
        }

        function sendMsgStop(stop_msg, machine){
            let url = "http://192.168.0.198:8000/control/msg_pause/";
            let params = "&stop_msg=" + stop_msg + "&machine=" + machine;
            console.log('send command');
        
            // var params = "lorem=ipsum&name=alpha";
            let xhr = new XMLHttpRequest();
            xhr.open("POST", url, true);

            //Send the proper header information along with the request
            xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

            xhr.send(params);
        }


        
        function msg_summary(){
            listaMensajes = [];
            time_msg = `${horas}:${minutos}:${segundos}`;
            time_paused_msg = `${horas_stoped}:${minutos_stoped}:${segundos_stoped}`;

            var today = new Date();
            var now = today.toLocaleString();
            start_hour = sessionStorage.getItem("vf2_startTime");
            listaMensajes.push(
                ("--------------------------------"),
                ("Tiempo activo: "+time_msg),
                ("Tiempo parado: "+time_paused_msg),
                ("Final: "+now),
                ("Inicio: "+start_hour),
                ("Maquina: vf2"),
                ("Codigo de pieza: AR-FRE-"+input_codigo_pieza.value),
                ("--------------------------------"),
                );
            return listaMensajes
        }

        function msg_pause(old_value){
            listaMensajesPausa = [];
            var today = new Date();
            var now = today.toLocaleString();
            listaMensajesPausa.push(
                ("--------------------------------"),
                (now+" : "+input_pause_motive.value),
                ("--------------------------------"),
                );
            // console.log(listaMensajesPausa,);
            return listaMensajesPausa
        }


        function InsertarTexto(msg,pause) {
            // console.log(msg);
            if (pause == true){
                var ul = document.getElementById("cuadroMensajes");
            } else {
                var ul = document.getElementById("cuadroMensajesPausa");
            }
            if (ul){
              for (let i = 0; i < msg.length; i++) {
                  const li = document.createElement("li");
                  li.setAttribute("style", "list-style: none;" );
                  li.innerHTML = msg[i];
                  ul.prepend(li);
              }
            }
            else{
              console.log('No hay mensaje');
            }
        }

        function sendCommandTimervf2(timer_vf2,machine){
            let url = "http://192.168.0.198:8000/control/timer_vf4/";
            let params = "&timer_vf2=" + timer_vf2 + "&machine=" + machine;
            console.log('send command');
        
            // var params = "lorem=ipsum&name=alpha";
            let xhr = new XMLHttpRequest();
            xhr.open("POST", url, true);
        
            //Send the proper header information along with the request
            xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        
            xhr.send(params);
        }

        function sendFinishStartPiecevf2(state,machine){
            let url = "http://192.168.0.198:8000/control/finish_start_vf4/";
            let params = "&state=" + state + "&machine=" + machine;;
            console.log('send command');
        
            // var params = "lorem=ipsum&name=alpha";
            let xhr = new XMLHttpRequest();
            xhr.open("POST", url, true);
        
            //Send the proper header information along with the request
            xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

            xhr.send(params);
        }

        function sendSelectedPiece(piece,machine){
            let url = "http://192.168.0.198:8000/control/selected_piece/";
            let params = "&piece=" + piece + "&machine=" + machine;
            console.log('send command');
        
            // var params = "lorem=ipsum&name=alpha";
            let xhr = new XMLHttpRequest();
            xhr.open("POST", url, true);
        
            //Send the proper header information along with the request
            xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

            xhr.send(params);
        }


        



        
   
});


function vf2(dataWs) {
    console.log(dataWs.vf2_piece);
    horas = dataWs.timer_vf2["horas"];
    minutos = dataWs.timer_vf2["minutos"];
    segundos = dataWs.timer_vf2["segundos"];
    horas_stoped = dataWs.timer_vf2["horas_stoped"];
    minutos_stoped = dataWs.timer_vf2["minutos_stoped"];
    segundos_stoped = dataWs.timer_vf2["segundos_stoped"];
    // console.log((sessionStorage.getItem("vf2_startTime")),(start_hour));
    // console.log(typeof(sessionStorage.getItem("vf2_startTime")),typeof(start_hour));
    


    document.getElementById("seconds").innerHTML = segundos < 10 ? "0" + segundos : segundos;
    document.getElementById("hours").innerHTML = horas < 10 ? "0" + horas : horas;
    document.getElementById("minutes").innerHTML = minutos < 10 ? "0" + minutos : minutos;

    document.getElementById("seconds_stoped").innerHTML = segundos_stoped < 10 ? "0" + segundos_stoped : segundos_stoped;
    document.getElementById("hours_stoped").innerHTML = horas_stoped < 10 ? "0" + horas_stoped : horas_stoped;
    document.getElementById("minutes_stoped").innerHTML = minutos_stoped < 10 ? "0" + minutos_stoped : minutos_stoped;

    document.getElementById("piece_code").innerHTML = dataWs.vf2_piece
}

 

