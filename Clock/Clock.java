public class Clock
{
	//attributes
	private int minutes;// PRIVATE MEANS YOU CAN ONLY ACCESS IT IN THIS CLASSS
	private int seconds;
	private int hours;
	private int milliseconds;


	//methods
	public Clock()
	{
	}//end of constructor method 
	
	
	
	public void increment(int s) 	
	{
		
		
		milliseconds  +=1; // adds 5 seconds to the variable
		
		while (milliseconds >= 100)
		{
			seconds +=1;
			milliseconds -=100;
		}
		
		while (seconds >= 60) //it while loop 
		{
			minutes +=1;
			seconds -=60;
			
		}
		
		while(minutes >= 60)
		{
			hours +=1;
			minutes -=60;
		}
	}
	
	public void increment()// no returns
	{
		increment(1); // make sure it's compatible
	}
	
	public void setTime(int h, int m, int s, int ms) // gave name as s, h and m
	{
		hours = h;
		minutes = m;
		seconds = s;
		milliseconds = ms;
	}//end of setTime
	
	public String getTime() 
	{
		String s = "";
		String m = "";
		String h = "";
		String ms = "";
		if (milliseconds < 10)
		{
			ms = "0";
		}
		
		if (seconds < 10) 
		{
			s = "0";
		}
		
		if (minutes < 10)
		{
			m = "0";
		}
		
		if (hours < 10)
		{
			h = "0";
		}
		return h + hours +  ":" + m + minutes + ":" + s + seconds + ":" + ms + milliseconds;
	}
	
	
}
