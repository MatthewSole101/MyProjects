public class Simulation
{
    Atom[] atoms = new Atom[100];


    public Simulation()
    {
        for (int i=0; i<atoms.length; i++)
        {
            atoms[i] =  new Atom(0.1);
        }
    }

    public int countUndecayedAtoms()
    {
        int count = 0;
        for(Atom a: atoms)
        {
            if(a.getDecayed() == false)
                count++;
        }
        return count;
    }

    public void tick()
    {
        for(Atom a: atoms)
        {
            a.decay();
        }
    }

    public static void main(String[] args)
    {
        Simulation bill = new Simulation();
        for(int i=0; i<20; i++)
        {
            bill.tick();
            System.out.println(bill.countUndecayedAtoms()+" atoms undecayed");
        }
    }
}
