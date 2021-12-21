function weatherInfo(weather,country,day){
	var today = new Date();
	var time = today.getHours();
	var i;
	var todayMaxT,todayMinT,todayPOR,todayCI,todayWP,
		secondMaxT,secondMinT,secondPOR,secondCI,secondWP;
	if(time>=0 && time<6)
	{
		todayPOR=(parseInt(weather[country+17])+parseInt(weather[country+20]))/2;
		secondPOR=parseInt(weather[country+23]);
		todayMaxT=(parseInt(weather[country+47])+parseInt(weather[country+50]))/2;
		secondMaxT=parseInt(weather[country+53]);
		todayMinT=(parseInt(weather[country+27])+parseInt(weather[country+30]))/2;
		secondMinT=parseInt(weather[country+33]);
		todayCI=weather[country+37];
		secondCI=weather[country+43];
		todayWP=weather[country+4];
		secondWP=weather[country+12];
	}	
	else if(time>=6 && time<24)
	{
		todayPOR=parseInt(weather[country+17]);
		secondPOR=(parseInt(weather[country+23])+parseInt(weather[country+20]))/2;
		todayMaxT=(parseInt(weather[country+47]));
		secondMaxT=(parseInt(weather[country+53])+parseInt(weather[country+50]))/2;
		todayMinT=parseInt(weather[country+27]);
		secondMinT=(parseInt(weather[country+33])+parseInt(weather[country+30]))/2;
		todayCI=weather[country+37];
		secondCI=weather[country+43];
		todayWP=weather[country+4];
		secondWP=weather[country+12];
	}
	if(day==1)
		return [todayMaxT,todayMinT,todayPOR,todayCI,todayWP];
	else
		return [secondMaxT,secondMinT,secondPOR,secondCI,secondWP];
}