import java.awt.Color;
import java.io.File;


import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;


public class Ball
{
    private int myxpos;
    private int myypos;
    private int myxspeed;
    private int myyspeed;
    private int mySize;
    private int myballs;
    private Color myColor;

    public void myxpos(int x)
    {
        myxpos = x;
    }

    public int getmyxpos ()
    {
        return myxpos;
    }

    //
    public void myypos(int y)
    {
        myypos = y;
    }

    public int getmyypos ()
    {
        return myypos;
    }

//

    public void myxspeed(int x)
    {
        myxspeed = x;
    }

    public int getmyxspeed ()
    {
        return myxspeed;
    }

//

    public void myyspeed(int x)
    {
        myyspeed = x;
    }

    public int getmyyspeed ()
    {
        return myyspeed;

    }

//    public void myballs(int x)
//    {
//        myballs = x;
//    }
//    private int getMyballs()
//    {
//        return myballs;
//    }
//

    public void mySize(int x)
    {
        mySize = x;
    }

    public int getmySize ()
    {
        return mySize;
    }

    public void myColor(Color x)
    {
        myColor = x;
    }

    public Color getmyColor ()
    {
        return myColor;
    }
    public void makeSound2()
    {
        File file2 = new File("BigWill.wav");
        try
        {
        Clip clip = AudioSystem.getClip();
        clip.open(AudioSystem.getAudioInputStream(file2));
        clip.start();
        }catch (Exception e) {
        	e.printStackTrace();


        }
    }

    public void updatePosition(int panelWidth, int panelHeight)
    {
        // TODO Auto-generated method stub
        myxpos += myxspeed;
        myypos += myyspeed;


        if (this.getmyxpos() < 0)
        {
            this.myxspeed(this.getmyxspeed() *-1);
            this.myColor(Color.MAGENTA);
            makeSound2();

        }

        if (this.getmyxpos() > panelWidth-mySize)
        {

            this.myxspeed(this.getmyxspeed() *-1);
            this.myColor(Color.YELLOW);
            makeSound2();


        }

        if (this.getmyypos() < 0)
        {
            this.myyspeed(this.getmyyspeed() *-1);
            this.myColor(Color.RED);
            makeSound2();


        }

        if (this.getmyypos() > panelHeight-mySize)
        {
            this.myyspeed(this.getmyyspeed() *-1);
            this.myColor(Color.BLUE);
            makeSound2();

        }

    }










}
