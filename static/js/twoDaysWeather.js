function now()
{
	var time = today.getFullYear()+'-'+(today.getMonth() < 10 ? '0' : '')+(today.getMonth()+1)+'-'+
			(today.getDate() < 10 ? '0' : '')+today.getDate()+" "+(today.getHours() < 10 ? '0' : '')+
			today.getHours() + ":" +(today.getMinutes() < 10 ? '0' : '')+ today.getMinutes() + ":" +
			(today.getSeconds() < 10 ? '0' : '')+ today.getSeconds();	
	return time;
}
