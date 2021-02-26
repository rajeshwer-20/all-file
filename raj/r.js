var xx=0;
let y=[]
var c="______"
var x="aadbad"
let xi="aadbad"
let a=()=>{ 
    let y=document.getElementById('click').value
    yt(y)
}
let yt=(y)=>{
        document.getElementById('click').value=""  
        x="aadbad"
        if (x.includes(y)){
            for (var ii=0;ii<x.length;ii++){
                if (y!=x[ii]){
                    x=x.replace(x[ii],"_")
                }
            }
		    c=c.split("")
		    for (var i=0;i<x.length;i++){
		        if (x[i]!=c[i]){
    		        }if (x[i]=="_"){
    		            c[i]=c[i]
    		            }else{
    		                c[i]=x[i]
    		                }
			}
			c=c.toString()
            c=c.replaceAll(",","")
            if (c==xi){
            	document.querySelector(".a").textContent=c;
				document.querySelector(".uy").textContent="crongulation you win the game";
			}else{document.querySelector(".a").textContent=c;}
        }else{
            let k=["./HANGMAN PICS/1.png","./HANGMAN PICS/2.png","./HANGMAN PICS/3.png","./HANGMAN PICS/4.png","./HANGMAN PICS/5.png","./HANGMAN PICS/6.png","./HANGMAN PICS/7.png"]
            xx++
            if (xx==6){
                yy=xx
                let bb= document.getElementById('l').src=String(k[yy]) 
                document.querySelector(".kl").textContent="game over";
                document.querySelector(".a").textContent=x+"   thish is your word";   
                xx=0                      
            }else{
                let bb= document.getElementById('l').src=String(k[xx])
            }
        }

    b=''
}
let sd=()=>{
    xx=-1
    document.querySelector(".kl").textContent="";
    document.querySelector(".uy").textContent="";
    document.querySelector(".a").textContent="";
    x="aadbad"
    c="______"
    document.querySelector(".uu").textContent=""
	document.getElementById('click').value=''
	document.getElementById('l').src="./HANGMAN PICS/1.png"
}
let ur=()=>{
	console.log(c,"kfaktfkq")
	var cde=c
	c=c.replaceAll("_","")
	c=c.split("")
	for (var i=0;i<c.length;i++)
		console.log(xi)
		xi=xi.replace(c[i],"")
	xi=xi.split("")
	var kli=Math.floor((Math.random()*xi.length-1))
	y=xi[kli]
	xi=xi.toString()
	xi=xi.replaceAll(",","")
	c=cde
	console.log(c,"yit")
	if (c==xi){
		yt(y)
	}
	yt(y)
}