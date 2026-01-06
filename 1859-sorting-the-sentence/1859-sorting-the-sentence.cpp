class Solution {
public:
    string sortSentence(string s) {
        unordered_map<string,int> mp;
          stringstream ss(s);
          string word;
          string st="";
          vector<string> v;
      
          while(ss >> word){
             int dig=word[word.length()-1]-'0';
             
             string w=word.substr(0,word.length()-1);
             mp[w]=dig;
            v.push_back(w);
          }
         
          sort(v.begin(),v.end(),[&](string a,string b){
            return mp[a] < mp[b];
          });
          for(int i=0;i<v.size();i++){
            st+=v[i]+" ";
          }
            st.pop_back();
            return st;
    }
};