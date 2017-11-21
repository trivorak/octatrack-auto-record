var minutes = parseInt(prompt("Total Minutes?"));
var seconds = parseInt(prompt("Seconds?"));
var songLength = (minutes * 60) + seconds;
var spacing = 5;
var songLocation = 0;
var actionMarkerId = " !_e09b49b56869964487d5db37808e0667";

console.log('1 ' + songLocation + ' "Track 1 Audio" 0 1 0');
songLocation = addSongLength(songLocation);
console.log('9 ' + songLocation + actionMarkerId + ' 0 1 0');
songLocation = addSpacingLength(songLocation);
console.log('2 ' + songLocation + ' "Track 2 Audio" 0 1 0');
songLocation = addSongLength(songLocation);
console.log('10 ' + songLocation + actionMarkerId + ' 0 1 0');
songLocation = addSpacingLength(songLocation);
console.log('3 ' + songLocation + ' "Track 3 Audio" 0 1 0');
songLocation = addSongLength(songLocation);
console.log('11 ' + songLocation + actionMarkerId + ' 0 1 0');
songLocation = addSpacingLength(songLocation);
console.log('4 ' + songLocation + ' "Track 4 Audio" 0 1 0');
songLocation = addSongLength(songLocation);
console.log('12 ' + songLocation + actionMarkerId + ' 0 1 0');
songLocation = addSpacingLength(songLocation);
console.log('5 ' + songLocation + ' "Track 5 Audio" 0 1 0');
songLocation = addSongLength(songLocation);
console.log('13 ' + songLocation + actionMarkerId + ' 0 1 0');
songLocation = addSpacingLength(songLocation);
console.log('6 ' + songLocation + ' "Track 6 Audio" 0 1 0');
songLocation = addSongLength(songLocation);
console.log('14 ' + songLocation + actionMarkerId + ' 0 1 0');
songLocation = addSpacingLength(songLocation);
console.log('7 ' + songLocation + ' "Track 7 Audio" 0 1 0');
songLocation = addSongLength(songLocation);
console.log('15 ' + songLocation + actionMarkerId + ' 0 1 0');
songLocation = addSpacingLength(songLocation);
console.log('8 ' + songLocation + ' "Track 8 Audio" 0 1 0');
songLocation = addSongLength(songLocation);
console.log('16 ' + songLocation + ' !1016 0 1 0');



function addSongLength(time){
	return time + songLength;
}

function addSpacingLength(time){
	return time + spacing;
}