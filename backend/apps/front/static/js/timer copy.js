window.addEventListener("DOMContentLoaded", () => {
    (window.location.hash);
        let horas = 0;
        let minutos = 0;
        let segundos = sessionStorage.getItem("vf4_timer");
        let horas_stoped = 0;
        let minutos_stoped = 0;
        let segundos_stoped = 0;
        btn_reset = document.getElementById("btn_reset")
        btn_pause = document.getElementById("btn_pause")
        btn_start = document.getElementById("btn_start")
        btn_select = document.getElementById("btn_select")
        input_tiempo_estimado = document.getElementById("tiempo_estimado")
        input_codigo_pieza = document.getElementById("codigo_pieza")
        var isPaused = false;
        var isReseted = false;
        var first_row = 0;
        var presed_button = true;
        document.getElementById("seconds").innerHTML = sessionStorage.getItem("vf4_timer")


        // if (presed_button == true && !isReseted && !isPaused) {
            
        // }

        // if (!sessionStorage.getItem("start_presed")) {
        //     sessionStorage.setItem("vf4_timer", "");
        // }

    
    
        function actualizarCronometro() {
            function sendCommandTimerVF2(timer_vf2){
                let url = "http://192.168.0.198:8000/control/timer_vf2/";
                let params = "&timer_vf2=" + timer_vf2;
                console.log('send command');
            
                // var params = "lorem=ipsum&name=alpha";
                let xhr = new XMLHttpRequest();
                xhr.open("POST", url, true);
            
                //Send the proper header information along with the request
                xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
            
                xhr.send(params);
            }
            
            if (!isReseted) {
                if (!isPaused) {
                    segundos++;
                    if (segundos >= 60) {
                        segundos = 0;
                        minutos++;
                        if (minutos >= 60) {
                        minutos = 0;
                        horas++;
                        if (horas >= 24) {
                            horas = 0;
                        }
                        }
                    }
                    current_value = sessionStorage.getItem("vf4_timer");
                    document.getElementById("hours").innerHTML = horas < 10 ? "0" + horas : horas;
                    document.getElementById("minutes").innerHTML = minutos < 10 ? "0" + minutos : minutos;
                    document.getElementById("seconds").innerHTML = sessionStorage.getItem("vf4_timer") < 10 ? "0" + segundos : segundos;
                    // document.getElementById("seconds").innerHTML = segundos < 10 ? "0" + segundos : segundos;
                    var start = Date.now();
                    sendCommandTimerVF2(sessionStorage.getItem("vf4_timer"))
                    var end = Date.now();
                    console.log("the timeeeeeeeeeeee",end - start);
                    sessionStorage.setItem("vf4_timer", segundos);
                } else {
                    segundos_stoped++;
                    if (segundos_stoped >= 60) {
                        segundos_stoped = 0;
                        minutos_stoped++;
                        if (minutos_stoped >= 60) {
                            minutos_stoped = 0;
                            horas_stoped++;
                        if (horas_stoped >= 24) {
                            horas_stoped = 0;
                        }
                        }
                    }
                    document.getElementById("hours_stoped").innerHTML = horas_stoped < 10 ? "0" + horas_stoped : horas_stoped;
                    document.getElementById("minutes_stoped").innerHTML = minutos_stoped < 10 ? "0" + minutos_stoped : minutos_stoped;
                    document.getElementById("seconds_stoped").innerHTML = segundos_stoped < 10 ? "0" + segundos_stoped : segundos_stoped;
    
                }
            }
        }
    
        
        btn_start.addEventListener("click", (e) => {
            console.log('boton start pulsado');
            if (first_row == 0) {
                console.log('run');
                setInterval(actualizarCronometro, 1000);
                presed_button = false;
            }
            isPaused = false
            isReseted = false
            first_row ++
            document.getElementById("pause_state").style.backgroundColor  = '#31af03'
            // document.getElementById("pause_state").style.visibility = 'hidden'

            if (!sessionStorage.getItem("vf4_timer")) {
                sessionStorage.setItem("vf4_timer", "");
            } else {

            }
    
        });
    
        btn_pause.addEventListener("click", (e) => {
            console.log('boton pause pulsado');
            actualizarCronometro(true)
            isPaused = true
            document.getElementById("pause_state").style.backgroundColor  = '#ff0000'
            // document.getElementById("pause_state").style.visibility = 'visible'
        });
    
        btn_reset.addEventListener("click", (e) => {
            horas = 0;
            minutos = 0;
            segundos = 0;
            horas_stoped = 0;
            minutos_stoped = 0;
            segundos_stoped = 0;
            document.getElementById("hours").innerHTML = horas < 10 ? "0" + horas : horas;
            document.getElementById("minutes").innerHTML = minutos < 10 ? "0" + minutos : minutos;
            document.getElementById("seconds").innerHTML = segundos < 10 ? "0" + segundos : segundos;
            document.getElementById("hours_stoped").innerHTML = horas_stoped < 10 ? "0" + horas_stoped : horas_stoped;
            document.getElementById("minutes_stoped").innerHTML = minutos_stoped < 10 ? "0" + minutos_stoped : minutos_stoped;
            document.getElementById("seconds_stoped").innerHTML = segundos_stoped < 10 ? "0" + segundos_stoped : segundos_stoped;
            isReseted = true
        });



        // input_codigo_pieza.addEventListener("input", (event) => {
        //     document.getElementById("piece_code").innerHTML = input_codigo_pieza.value
        //     // console.log(input_codigo_pieza.value);
        // });


        btn_select.addEventListener("click", (event) => {
            document.getElementById("piece_code").innerHTML = input_codigo_pieza.value
            // console.log(input_codigo_pieza.value);
        });


        // console.log(input_codigo_pieza.value)
        
     
    
        // window.onload = function() {
        //     setInterval(actualizarCronometro, 1000);
        // };

        
    
    
    

    // // Obtener elementos de span
    // const hoursSpan = document.getElementById('hours');
    // const minutesSpan = document.getElementById('minutes');
    // const secondsSpan = document.getElementById('seconds');

    // // Establecer la cuenta regresiva
    // let timeLeft = 3600; // 1 hora en segundos

    // const countdown = setInterval(() => {
    // // Obtener horas, minutos y segundos restantes
    // const hoursLeft = Math.floor(timeLeft / 3600);
    // const minutesLeft = Math.floor((timeLeft % 3600) / 60);
    // const secondsLeft = timeLeft % 60;

    // // Actualizar los elementos de span con las horas, minutos y segundos restantes
    // hoursSpan.textContent = hoursLeft < 10 ? `0${hoursLeft}` : hoursLeft;
    // minutesSpan.textContent = minutesLeft < 10 ? `0${minutesLeft}` : minutesLeft;
    // secondsSpan.textContent = secondsLeft < 10 ? `0${secondsLeft}` : secondsLeft;

    // // Disminuir el tiempo restante en 1 segundo
    // timeLeft--;

    // // Si el tiempo restante llega a 0, detener la cuenta regresiva
    // if (timeLeft < 0) {
    //     clearInterval(countdown);
    //     alert('Tiempo agotado');
    // }
    // }, 1000);

   
});


function timer(dataWs) {
    function sendCommandTimerVF2(timer_vf2){
        let url = "http://192.168.0.198:8000/control/timer_vf2/";
        let params = "&timer_vf2=" + timer_vf2;
        console.log('send command');
    
        // var params = "lorem=ipsum&name=alpha";
        let xhr = new XMLHttpRequest();
        xhr.open("POST", url, true);
    
        //Send the proper header information along with the request
        xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    
        xhr.send(params);
    }
    console.log(dataWs);
    // sendCommandTimerVF2(sessionStorage.getItem("vf4_timer"))
}

 

