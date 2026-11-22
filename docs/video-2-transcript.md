
00:00:03
This is the validation and sensitivity  demonstration for my Meridian Foundation  investment management application. My  goal was to make sure the calculations  are reproducible, the data limitations  are transparent, and the investment  recommendation does not depend on one  untested assumption. I used automated  testing, historical data checks, known  answer reconciliation,  and a logged change input experiment to  evaluate the application.


00:00:31
 I'll just uh now I'll move on to the  automated uh testing section of the  video.  During VS Code, I run the automated unit  tests for the portfolio model and the  data integrity checks. These tests  examine calculations, input validation,  and whether the application handles  important constraints correctly. The  test suit includes checks for portfolio  weights, transaction costs, point and  time timing, and the locked prediction  workflow.


00:00:57
 The tests passing show that  these programmed behaviors work under  the tested conditions. It does not  establish that the investment  assumptions are correct or that the  strategy will perform well in the  market.  I'll move on to the known answer  reconciliation part of the um video in  my VS code that is under the evidence  folder. This is the MD file.


00:01:20
 This is  what it basically is. And um next I  reconcile the project two portfolio  calculations against the known answers  from lab 14. For the equal weight  portfolio, the expected return is 5.20%  and the volatility is 5.21%. The  benchmark produces a 6.80% expected  return and a 10.46% volatility. These  match the previously reported classroom  calculations which help verify that the  project to model reproduces its sources  assumptions correctly.


00:01:51
 However, this is  a calculation reconciliation, not  independent market validation.  Moving on to stress testing and  sensitivity controls. Um, I will be  moving back to um stream this my  streamlit app for that.  Um,  all right. Returning to um the  streamllet this section. I'm going to  move on to the stress um test section.  This section basically allows me to test  how sensitive the portfolio results are  to changes in the model assumptions.


00:02:26
 I  can change transaction costs, expected  return assumptions, and correlations to  observe their effects on the portfolio.  These controls are useful because an  investment decision should not be based  only on a single base calculation. The  results are sensitivity scenarios. They  do not represent independently verified  forecasts or actual trading performance.


00:02:47
 Moving  on to the log changed input experiment.  Um I'll just show the completed results  from my um prediction. This is basically  what uh  came out of it.  to kind of summarize everything. Um the  most important numbers uh are the  transaction costs which went from 25 bps  to 50, the gross expected return um  which kind of remained the same, the  cost drag which decreased uh or  increased a little bit um the net  expected return also in decreased a  little bit and then the 6.


00:03:29
5% comparison  which remained a fail. So the most  important validation exercise is my log  changed input experiment. Before running  the experiment, I recorded a prediction  on GitHub, which allowed the prediction  to be compared with the actual model  output rather than being rewritten  afterwards. I tested what happens when  transaction costs increase from 25 to 50  basic points while annual turnover stays  at 25%.


00:03:52
 I predicted that the gross  expected return would remain unchanged  while net expected return would decline  from approximately 5.14% to 5.08%.  And after running the experiment, the  model produced a gross return of 5.20%  in both scenarios. Transaction cost drag  increased from 0.0625%  to 0.125% and net expected return  decreased from 5.


00:04:16
1375%  to 5.075%.  These results are supported by my these  results supported my earlier prediction.  Both scenarios still failed at the 6.5%  classroom comparison and the committee  recommendation remain unchanged which  was no pilot author authorization. This  demonstrates that implementation costs  matter even when the underlying  portfolio assumptions remain unchanged.


00:04:43
 Now I'll move on to um talking about  point in time data integrity and I will  just move on to um that section.  This is the DGS data warning that was  given by the app and all the signals  and values.  Um, another important validation issue  is of course point in time data  integrity. The application includes  DGS10 interest rate observations from  earlier lab work, but the available  vintage evidence is however incomplete.


00:05:26
 The application uses a timing control to  prevent the same day observation from  being treated as available before its  reported release time. However, a few  checked observations are not enough to  satis establish a complete point in time  history. For that reason, the signal  remains quarantined and cannot justify  an investment allocation.


00:05:46
 I just go back to the main page of the  top of my app which has this warning  which says pilot state is not  authorized. Um overall my tests and  reconciliation support the application's  calculation consistency and  reproducibility.  The changed input experiment also  confirm the predicted effect of higher  transaction costs.


00:06:06
 However, unresolved  data integrity and mandate compliance  questions prevent the portfolio from  being approved. Therefore, the  application maintains its recommendation  of no pilot authorization. This  concludes my validation uh  demonstration. Thank you.

