let numero = 0
input.onButtonPressed(Button.A, function () {
    numero = 0
    while (numero <= 10) {
        basic.showNumber(numero)
        basic.pause(1000)
        numero += 1
    }
    basic.pause(1000)
    basic.showString("FIM")
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function () {
    numero = 10
    while (numero >= 0) {
        basic.showNumber(numero)
        basic.pause(1000)
        numero += -1
    }
    basic.clearScreen()
    basic.pause(1000)
    basic.showString("FIM")
})
