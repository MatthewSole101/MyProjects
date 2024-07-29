using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using CMP1903_A1_2324.Properties;

namespace CMP1903_A1_2324
{
    internal class Testing
    {

        public static void Main(string[] args)
        {
            /*
             * This class should test the Game and the Die class.
             * Create a Game object, call the methods and compare their output to expected output.
             * Create a Die object and call its method.
             * Use debug.assert() to make the comparisons and tests.
             */

            //Creates instances of the 
            SevensOutStatistics mySevensOutStatisticsstats = new SevensOutStatistics();
            ThreeOrMoreStatistics myThreeOrMoreStatistics = new ThreeOrMoreStatistics();

            CheckStats SevensOutmenuStats = new CheckStats();
            CheckStatsThreeOrMore ThreeOrMoremenuStats = new CheckStatsThreeOrMore();

            //Method
            //
            int gameChoice = 0;

            try
            {
                Console.WriteLine("---------------------------------------------------------------------------------");
                Console.WriteLine("Do you want to play SevensOut(1) or Three or More(2) or check statistics(3)?: ");
                gameChoice = Convert.ToInt32(Console.ReadLine());
            }
            catch
            {
                Console.WriteLine("Invalid input");
                Console.WriteLine("Try again");
            }

            if (gameChoice == 1)
            {
                
            }
            


            ///////////////////////////////////














            if (gameChoice == 2)
            {
                //ThreeOrMore

                int threeOrMoreplayer1Score = 0;
                int threeOrMoreplayer2Score = 0;
                int count = 0;
                int uniqueNum = 0;




                while ((threeOrMoreplayer1Score <= 20) || (threeOrMoreplayer2Score <= 20))
                {

                    ThreeOrMore tom2 = new ThreeOrMore();

                    if (threeOrMoreplayer1Score < 20)
                    {
                        if (threeOrMoreplayer1Score >= 20)
                        {
                            break;
                        }


                        string player1exit = "";
                        //Error handling
                        try
                        {
                            Console.WriteLine("Do you want to roll(yes/no)?: ");
                            player1exit = Console.ReadLine();
                        }
                        catch
                        {
                            Console.WriteLine("Invalid input");
                            Console.WriteLine("Try again");
                        }



                        if (player1exit == "yes" || player1exit == "Yes")
                        {
                            bool player1exit2 = false;
                            while (player1exit2 == false)
                            {
                                Console.WriteLine("");
                                Console.WriteLine("-----Player 1-----");
                                Console.WriteLine("");
                                List<int> Player1RollThreeorMore = new List<int>();
                                uniqueNum = 0;

                                Player1RollThreeorMore = tom2.Player1game();


                                //Prints out all die rolls
                                for (int i = 0; i < 5; i++)
                                {
                                    Console.WriteLine(Player1RollThreeorMore[i]);
                                }

                                uniqueNum = tom2.checkUnique(Player1RollThreeorMore);



                                threeOrMoreplayer1Score = myThreeOrMoreStatistics.Player1Stat(uniqueNum, false);

                                if (threeOrMoreplayer1Score == 1)
                                {
                                    player1exit2 = false;

                                }
                                else
                                {
                                    player1exit2 = true;
                                }



                                Console.WriteLine("The dice are " + uniqueNum + " of a kind.");

                                Console.WriteLine("Player 1 has " + threeOrMoreplayer1Score + " points");

                            }


                        }

                        if (player1exit == "no" || player1exit == "No")
                        {
                            break;
                        }




                    }

                    else
                    {
                        break;
                    }



                    if (threeOrMoreplayer2Score < 20)
                    {
                        if (threeOrMoreplayer1Score >= 20)
                        {
                            break;
                        }


                        uniqueNum = 0;
                        string player2exit = "";
                        try
                        {
                            Console.WriteLine("Do you want to continue(yes/no)?: ");
                            player2exit = Console.ReadLine();
                        }
                        catch
                        {
                            Console.WriteLine("Invalid input");
                            Console.WriteLine("Try again");
                        }




                        if (player2exit == "yes" || player2exit == "Yes")
                        {
                            bool player2exit2 = false;
                            while (player2exit2 == false)
                            {
                                Console.WriteLine("");
                                Console.WriteLine("-----Player 2-----");
                                Console.WriteLine("");

                                List<int> Player2RollThreeorMore = new List<int>();

                                Player2RollThreeorMore = tom2.Player2game();


                                //Displays die rolls
                                for (int i = 0; i < 5; i++)
                                {
                                    Console.WriteLine(Player2RollThreeorMore[i]);
                                }

                                uniqueNum = tom2.checkUnique(Player2RollThreeorMore);

                                threeOrMoreplayer2Score = myThreeOrMoreStatistics.Player2Stat(uniqueNum, false);






                                if (threeOrMoreplayer2Score == 1)
                                {
                                    player2exit2 = false;


                                }
                                else
                                {
                                    player2exit2 = true;

                                }

                                Console.WriteLine("The dice are " + uniqueNum + " of a kind.");
                                Console.WriteLine("Player 2 has " + threeOrMoreplayer2Score + " points");
                            }


                        }

                        if (player2exit == "no" || player2exit == "No")
                        {
                            break;
                        }

                    }
                    else
                    {
                        break;
                    }


                }

                //When game is over it will display both players stats and who one
                int player1Score = myThreeOrMoreStatistics.Player1Stat(0, true);
                int player2Score = myThreeOrMoreStatistics.Player2Stat(0, true);

                if (player1Score > player2Score)
                {
                    Console.WriteLine("Player 1 wins!");
                }

                if (player1Score < player2Score)
                {
                    Console.WriteLine("Player 2 wins!");
                }

                //Asks the user if they want to play another game


            }

            if (gameChoice == 3)
            {

                //Checks stats in the menu
                //Uses Polymorphism to make it more understandle what is going on 
                int statChoice = 0;
                bool isStatChoice = false;
                while (isStatChoice == false)
                {
                    try
                    {
                        Console.WriteLine("Do you want to look at SevensOut(1) or ThreeOrMore(2)?: ");
                        statChoice = Convert.ToInt32(Console.ReadLine());
                    }
                    catch
                    {
                        Console.WriteLine("Invalid input");
                        Console.WriteLine("Try again");
                    }


                    if (statChoice == 1)
                    {
                        SevensOutmenuStats.SevensOutstats();
                        isStatChoice = true;
                    }

                    if (statChoice == 2)
                    {
                        ThreeOrMoremenuStats.ThreeOrMorestats();
                        isStatChoice = true;

                    }
                }



            }
        }

    }
}

