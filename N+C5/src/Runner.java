import javax.swing.JFrame;
import java.awt.Color;
public class Runner
{

    public static void main(String[] args)
    {
        // TODO Auto-generated method stub
        JFrame window = new JFrame();
        Interface io = new Interface();
        window.setContentPane(io);
        window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        window.setTitle("Noughts and Crosses");
        window.setSize(400,300);
        window.setVisible(true);
        window.setBackground(Color.black);
        
        
       

    }


}