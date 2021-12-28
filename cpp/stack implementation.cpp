#include <stdio.h>
#include<iostream>
using namespace std;
class stack{
    public:
    int top=-1,size=5,stk[10];
    void push();
    void pop();
    void display();
};
void stack::push(){
    int x;
    if(top==size-1)
    cout<<"stack full";
    else{
        cin>>x;
        top++;
        stk[top]=x;
    }
}
void stack::pop(){
    if(top==-1){
        cout<<"stack empty";
    }
    else{
        top--;
    }
}
void stack::display()
{
    if(top==-1){
        cout<<"stack empty";
    }
    else{
        int i;
        for(i=top;i>=0;i--){
            cout<<stk[i]<<endl;
        }
    }
}
int main()
{
    stack s;
    s.display();
    s.push();
    s.push();
    s.pop();
    s.push();
    s.pop();
    s.display();

    return 0;
}
