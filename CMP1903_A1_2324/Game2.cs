using System;

namespace CMP1903_A1_2324.Properties
{  
    public class Game2
    {


        static void GameSeven(int gameChoice = 0)
        {
            
            //SevensOut
            
            
            //Created a Game and SevensOut, Three Or More and stats object
            Game gm = new Game();
            SevensOut so = new SevensOut();
            ThreeOrMore tom = new ThreeOrMore();
            
            SevensOutStatistics mySevensOutStatisticsstats = new SevensOutStatistics();
            CheckStats SevensOutmenuStats = new CheckStats();

            
            
            bool isExit = false;
            bool sevensOutexit = false;
            
           
            
            bool menuExit = false;
            

            //Call the myMethod method and saving its return in Roll which is a tuple

            int totalroll = 0;
            

            int player1totalscore = 0;
            int player2totalscore = 0;
            
            while (isExit == false) 
                    {
                        //Continue to roll random die rills from the SevensOut class and saves them as a tuple
                        var Player1Roll = so.Player1game();
                        var Player2Roll = so.Player2game();

                        int player1CheckSeven = Player1Roll.Item1 + Player1Roll.Item2;
                        int player2CheckSeven = Player2Roll.Item1 + Player2Roll.Item2;

                        //Checks rolls and assignes the pints from Statistics class
                        if (player1CheckSeven == 7)
                        {
                            Console.WriteLine("");
                            Console.WriteLine("Player 1 die rolled are: " + Player1Roll.Item1 + " and " + Player1Roll.Item2);
                            sevensOutexit = true;
                            break;
                            
                        }
                        if (player2CheckSeven == 7)
                        {
                            Console.WriteLine("");
                            Console.WriteLine("Player 2 die rolled are: " + Player2Roll.Item1 + " and " + Player2Roll.Item2);
                            sevensOutexit = true;
                            break;
                            
                        }
                        
                        
                        if (Player1Roll.Item1 != 7 || Player2Roll.Item1 != 7)
                        {
                            if (Player1Roll.Item1 != 7)
                            {
                                if (Player1Roll.Item1 != Player1Roll.Item2)
                                {
                                    totalroll = Player1Roll.Item1 + Player1Roll.Item2;
                                    player1totalscore = mySevensOutStatisticsstats.Player1Stat(totalroll, false);
                                    Console.WriteLine("");

                                    Console.WriteLine("Player 1 die rolled are: " + Player1Roll.Item1 + " and " + Player1Roll.Item2);

                                }
                            }

                            if (Player2Roll.Item1 != 7)
                            {
                                if (Player2Roll.Item1 != Player2Roll.Item2)
                                {
                                    totalroll = Player2Roll.Item1 + Player2Roll.Item2;
                                    player2totalscore = mySevensOutStatisticsstats.Player2Stat(totalroll, false);
                                    Console.WriteLine("Player 2 die rolled are: " + Player2Roll.Item1 + " and " + Player2Roll.Item2);
                            
                                }
                            }
                           
                        }

                        if ( Player1Roll.Item1 == Player1Roll.Item2 ||Player2Roll.Item1 == Player2Roll.Item2)
                        {
                            if ( Player1Roll.Item1 == Player1Roll.Item2) 
                            {
                                totalroll = (Player1Roll.Item1 * 2) + (Player1Roll.Item1 * 2);
                                player1totalscore = mySevensOutStatisticsstats.Player1Stat(totalroll, false);                                Console.WriteLine("");
                                Console.WriteLine("");
                                Console.WriteLine("Player 1 die rolled are: " + Player1Roll.Item1 + " and " + Player1Roll.Item2);

                            }
                            if (Player2Roll.Item1 == Player2Roll.Item2)
                            {
                                totalroll = (Player2Roll.Item1 * 2) + (Player2Roll.Item1 * 2);
                                player2totalscore = mySevensOutStatisticsstats.Player2Stat(totalroll, false);
                                Console.WriteLine("Player 2 die rolled are: " + Player2Roll.Item1 + " and " + Player2Roll.Item2);
                            }
                           
                        }
                        

                        
                        while (sevensOutexit == false)
                        {
                            string userStatChoice = "";
                            //Error handling
                            try
                            {
                                Console.WriteLine("Do you want to look at your statistics(yes/no)?: ");
                                userStatChoice = Console.ReadLine();
                            }
                            catch
                            {
                                Console.WriteLine("Invalid input");
                                Console.WriteLine("Try again");
                            }
                            

                            

                            if (userStatChoice == "Yes" || userStatChoice == "yes")
                            {
                                //Polymorphism
                                //If the user says yes to checking stats - the Player stat method gets called. But because 'userStat' is true - it just checks the current stats
                                mySevensOutStatisticsstats.Player1Stat(0, true);
                                mySevensOutStatisticsstats.Player2Stat(0, true);


                            }
                            if (userStatChoice == "No" || userStatChoice == "no")
                            {
                                
                                break;
                            }
                           
                        }
                        

                    }
                    
                    Console.WriteLine("Player 1's total score is "+ player1totalscore);
                    Console.WriteLine("Player 2's total score is "+ player2totalscore);

                    if (player1totalscore > player2totalscore)
                    {
                        Console.WriteLine("");
                        Console.WriteLine("Player 1 is the winner!");
                    }

                    if (player1totalscore < player2totalscore)
                    {
                        Console.WriteLine("");
                        Console.WriteLine("Player 2 is the winner!");

                    }

                    if (player1totalscore == player2totalscore)
                    {
                        Console.WriteLine("");
                        Console.WriteLine("It's a draw!");
                    }
        }
    }
}