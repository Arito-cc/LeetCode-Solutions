class Solution {
    public int maxProfit(int[] prices) {
        
        int buy = prices[0];
        int sell = 0;
        int total = 0;

        for(int i = 1; i<prices.length;i++){
            if(buy<prices[i]){
                if(sell<(prices[i]-buy)){
                    sell = prices[i]-buy;
                }
                else{
                    buy=prices[i];
                    total+=sell;
                    sell =0;
                }
            }
            else{
                buy=prices[i];
                total+=sell;
                sell=0;
            }
        }

        
        total += sell;
        
        return total;
    }
}