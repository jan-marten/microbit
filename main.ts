let degrees = 0
input.onButtonPressed(Button.A, function () {
    basic.showString("A")
})
basic.forever(function () {
    degrees = Math.floor(input.compassHeading() / 52)
    basic.showArrow(degrees)
})
