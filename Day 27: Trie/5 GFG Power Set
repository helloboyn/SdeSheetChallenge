class Solution{
	public:
		vector<string> AllPossibleStrings(string s){
		    // Code here
		    vector<string> v;
		    int n = s.length();
		    int powSize = pow(2,n);
		  //  string str="";
		    for(int countNo=0;countNo<powSize;countNo++)
		    {
		        string str ="";
		        for(int j=0;j<n;j++)
		        {
		            if((countNo & (1<<j))!=0){
		             str+=s[j];
		            }
		        }
		        
		         if(str.length()>0)
		         v.push_back(str);
		    }
		    sort(v.begin(),v.end());
		    return v;
		}
};
