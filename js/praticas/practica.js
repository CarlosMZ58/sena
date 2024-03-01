function main() {
    var usuarioPonencia = createArray(5);
    var contadorUsuario;

    for (contadorUsuario = 0; contadorUsuario <= 4; contadorUsuario++) {
        usuarioPonencia[contadorUsuario] = window.prompt('Enter a value for usuarioPonencia[contadorUsuario]');
    }
    var usuarioBuscado;

    usuarioBuscado = window.prompt('Enter a value for usuarioBuscado');
    var contador;

    contador = 0;
    while (usuarioPonencia[contador] != usuarioBuscado && contador < 4) {
        contador = contador + 1;
    }
    if (usuarioPonencia[contador] == usuarioBuscado) {
        window.alert(usuarioBuscado + " si hara la ponencia");
    } else {
        window.alert(usuarioBuscado + " no hara la ponencia");
    }
}
