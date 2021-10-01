function waitingTime(tickets, p) {
     var alex = p;
     var totalPeople = tickets[0];
     var totalTime = 0;
     //best case, if jesse is first and only wants to buy 1 ticket.
     if((tickets[alex+1] === 1) && (alex === 0)) {
         return 1;
     } else {
         for(var i = 1; i <= totalPeople; i++) {
             //totalTime += tickets[i] < tickets[jessePosition] ? tickets[i] - tickets[jessePosition] : tickets[i];
             totalTime += Math.min(tickets[i], tickets[alex] - (i > alex));
         }
         console.log(totalTime);
         return totalTime;
     }
 }
 
 
 waitingTime([2,6,3,4,5],2);