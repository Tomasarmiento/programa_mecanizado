window.addEventListener("DOMContentLoaded", () => {
    (window.location.hash);
    const button_finish = document.getElementById("finish_nesting");
    const button_add = document.getElementById("add_piece");
    const nesting_input = document.getElementById("nesting_input");
    const nesting_a = document.getElementById("nesting_a");
    const nesting_b = document.getElementById("nesting_b");
    const nesting_c = document.getElementById("nesting_c");
    const nesting_d = document.getElementById("nesting_d");
    const nesting_col_a = document.getElementById("nesting_col_a");
    const nesting_col_b = document.getElementById("nesting_col_b");
    const nesting_2mm = document.getElementById("nesting_2mm");
    const piece_input = document.getElementById("piece_input");
    var selected_value = ""
    var selected_multiply_value = 1
    var max_archa_pieces = 180


    button_finish.addEventListener("click", (e) => {
        if (confirm(`estas seguro que terminaste el nesting ${selected_value}?`)) {
            sendCommandNesting(selected_value)
            // setInterval(alert("CARGANDO"), 5000);
        }
        else {
            console.log("Cancelled");
        }
    });

    button_add.addEventListener("click", (e) => {
        if (confirm(`AR-CHA-${piece_input.value} / CANTIDAD = ${selected_multiply_value}`)) {
            // sendCommandSemi(selected_value)
            sendCommandPiece(piece_input.value,selected_multiply_value)
        }
        else {
            console.log("Cancelled");
        }
    });

    piece_input.addEventListener("input", (event) => {
        console.log(piece_input.value);
        if (piece_input.value > max_archa_pieces || piece_input.value < 0) {
            alert("error en codigo de pieza!")
            piece_input.value = 0
        } else {
            

            
        }
        // document.getElementById("piece_code").innerHTML = input_codigo_pieza.value
    });


    

    const controles = document.querySelector("#container_multiply");
    controles.addEventListener("click", (e) => {
        switch (e.target.id) {
          case "multiply_1":
            console.log("1");
            selected_multiply_value = 1
            break;
          case "multiply_2":
            console.log("2");
            selected_multiply_value = 2
            break;
          case "multiply_3":
            console.log("3");
            selected_multiply_value = 3
            break;  
          case "multiply_4":
            console.log("4");
            selected_multiply_value = 4
            break;
          case "multiply_5":
            console.log("5");
            selected_multiply_value = 5
            break;
          case "multiply_6":
            console.log("6");
            selected_multiply_value = 6
            break;
          case "multiply_7":
            console.log("7");
            selected_multiply_value = 7
            break;
          case "multiply_8":
            console.log("8");
            selected_multiply_value = 8
            break;
          case "multiply_9":
            console.log("9");
            selected_multiply_value = 9
            break;
          case "multiply_10":
            console.log("10");
            selected_multiply_value = 10
            break;
        }
        document.getElementById("multiply_leyend").innerHTML = "*"+selected_multiply_value

    });





    nesting_a.addEventListener("click", (e) => {
        selected_value = "nesting_a"
        nesting_input.value = "nesting_a"
    });
    nesting_b.addEventListener("click", (e) => {
        selected_value = "nesting_b"
        nesting_input.value = "nesting_b"
    });
    nesting_c.addEventListener("click", (e) => {
        selected_value = "nesting_c"
        nesting_input.value = "nesting_c"
    });
    nesting_d.addEventListener("click", (e) => {
        selected_value = "nesting_d"
        nesting_input.value = "nesting_d"
    });
    nesting_col_a.addEventListener("click", (e) => {
        selected_value = "nesting_col_a"
        nesting_input.value = "nesting_col_a"
    });
    nesting_col_b.addEventListener("click", (e) => {
        selected_value = "nesting_col_b"
        nesting_input.value = "nesting_col_b"
    });
    nesting_2mm.addEventListener("click", (e) => {
        selected_value = "nesting_2mm"
        nesting_input.value = "nesting_2mm"
  });


    



    function sendCommandNesting(nesting_value){
        let url = "http://192.168.0.198:8000/control/nesting_select/";
        let params = "&nesting_value=" + nesting_value;
        console.log('send command');
    
        // var params = "lorem=ipsum&name=alpha";
        let xhr = new XMLHttpRequest();
        xhr.open("POST", url, true);
    
        //Send the proper header information along with the request
        xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    
        xhr.send(params);
    }


    function sendCommandPiece(piece_code,cantidad){
        let url = "http://192.168.0.198:8000/control/piece_select/";
        let params = "&piece_code=" + piece_code + "&cantidad=" + cantidad;;
        console.log('send command');
    
        // var params = "lorem=ipsum&name=alpha";
        let xhr = new XMLHttpRequest();
        xhr.open("POST", url, true);
    
        //Send the proper header information along with the request
        xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    
        xhr.send(params);
    }




    
});