var m=180, n=0,r=20, s=50; x,y;

function setup(){
	createCanvas(300, 300);
	background(255,0,0);
	strokeWeight(1);
}

function draw(){
ellipse(150,150,5,5);
x= 150+r*cos(m);
y= 150+s*sin(m);
m=m+0.1;
ellipse(x, y, 5, 5);

}
