public class Atom {
    private boolean isDecayed = false;
    private double decayProb;



    public Atom(double prob)
    {
        decayProb = prob;





    }



    public void decay()
    {
        double Random = Math.random();
        if (Random < decayProb)
        {
            isDecayed = true;
        }


    }
    public void isDecayed()
    {
        isDecayed = false;
    }

    public boolean getDecayed()
    {
        return isDecayed;
    }

//    public void setDecayed()
//    {
//
//    }





}

