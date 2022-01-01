var game = new Phaser.Game(480, 320, Phaser.AUTO, null, {preload: preload, create: create, update: update});

var ball;
function preload() {
	// handleRemoteImagesOnJSFiddle();
    // game.scale.scaleMode = Phaser.ScaleManager.SHOW_ALL;
    // game.scale.pageAlignHorizontally = true;
    // game.scale.pageAlignVertically = true;
    game.stage.backgroundColor = '#ddd';
    game.load.image('ball2', 'img/simu.jpg');
}
function create() {
    ball = game.add.sprite(10, 10, 'ball2');
}
function update() {
    ball.x += 1;
    ball.y += 1;
}

// // this function (needed only on JSFiddle) take care of loading the images from the remote server
function handleRemoteImagesOnJSFiddle() {
	// game.load.baseURL = 'https://end3r.github.io/Gamedgaev-Phaser-Content-Kit/demos/';
	game.load.crossOrigin = 'anonymous';
}