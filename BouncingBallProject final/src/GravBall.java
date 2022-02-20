import java.awt.Color;
import java.io.File;


import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;

public class GravBall
{
    private int mygravballxpos;
    private int mygravballypos;
    private int mygravballxspeed;
    private int mygravballyspeed;
    private int mygravballSize;
    private Color mygravballColor;
    private int myceilingypos;

    public void mygravballxpos(int x)
    {
        mygravballxpos = x;
    }

    public int getmygravballxpos ()
    {
        return mygravballxpos;
    }

    //
    public void mygravballypos(int y)
    {
        mygravballypos = y;
    }

    public int getmygravballypos ()
    {
        return mygravballypos;
    }

//

    public void mygravballxspeed(int x)
    {
        mygravballxspeed = x;
    }

    public int getmygravballxspeed ()
    {
        return mygravballxspeed;
    }

//

    public void mygravballyspeed(int x)
    {
        mygravballyspeed = x;
    }

    public int getmygravballyspeed ()
    {
        return mygravballyspeed;

    }

//

    public void mygravballSize(int x)
    {
        mygravballSize = x;
    }

    public int getmygravballSize ()
    {
        return mygravballSize;
    }

    public void mygravballColor(Color x)
    {
        mygravballColor = x;
    }

    public Color getmygravballColor ()
    {
        return mygravballColor;
    }

    public void myceilingypos (int y)
    {
        myceilingypos = y;
    }

    public int getmyceilingpyos ()
    {
        return myceilingypos;
    }
    public void makeSound()
    {
        File file = new File("BigWill.wav");
        try
        {
            Clip clip = AudioSystem.getClip();
            clip.open(AudioSystem.getAudioInputStream(file));
            clip.start();
        }catch (Exception e) {
            e.printStackTrace();


        }
    }




    public void updatePosition(int panelWidth, int panelHeight)
    {
        mygravballxpos += mygravballxspeed;
        mygravballypos += mygravballyspeed;

//		int ceiling = this.getmygravballypos();

        if (this.getmygravballxpos() < this.getmyceilingpyos())
        {
            this.mygravballxspeed(this.getmygravballxspeed() *-1);
            this.myceilingypos(this.getmyceilingpyos() -10);
            this.mygravballColor(Color.MAGENTA);
            makeSound();

        }

        if (this.getmygravballxpos() > 380)
        {

            this.mygravballxspeed(this.getmygravballxspeed() *-1);
            this.mygravballColor(Color.YELLOW);
            makeSound();

        }

        if (this.getmygravballypos() < 0)
        {
            this.mygravballyspeed(this.getmygravballyspeed() *-1);
//			this.getmygravballypos(ceiling -1);
            this.mygravballColor(Color.RED);
            makeSound();

        }

        if (this.getmygravballypos() > 250)
        {
            this.mygravballyspeed(this.getmygravballyspeed() *-1);
            this.mygravballColor(Color.BLUE);
            makeSound();
        }
    }
}
