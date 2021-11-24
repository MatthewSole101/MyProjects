import javax.swing.*;

public class Tile extends JButton
{
    private char mySymbol;
    private String setText;
    private boolean isAvailable = false;

    public void setSymbol(char s)
    {
        mySymbol=s;
        this.setText(""+s);
        this.setEnabled(false);
    }

    public char getSymbol()
    {
        return mySymbol;
    }

    public void clear()
    {
        mySymbol = ' ';
        this.setText("");
    }



}