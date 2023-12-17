#include<stdio.h>
#include<stdlib.h>
#include<string.h>

typedef struct node
{
    char val;
    struct node* next;
}pnode;

typedef struct seqstack
{
    int size;
    pnode* top;
}phead;

phead* initstack()
{
    phead* istack=(phead*)malloc(sizeof(phead));
    if(istack!=NULL)
    {
        istack->top=NULL;
        istack->size=0;
    }
    return istack;
}

int isempty(phead* istack)
{
    if(istack->top==NULL)
    {
        return 1;
    }
    return 0;
}

pnode* seqstack_top(phead* istack)
{
    if(istack->size!=0)
    {
        return istack->top;
    }
    return NULL;
}

pnode* seqstack_pop(phead* istack)
{
    if(isempty(istack)==0)
    {
        pnode* account=istack->top;
        istack->top=istack->top->next;
        istack->size--;
        return account;
    }
    return NULL;
}

void seqstack_push(phead* istack,char x)
{
   pnode* temp;
   temp=(pnode*)malloc(sizeof(pnode));
   temp->val=x;
   temp->next=istack->top;
   istack->top=temp;
   istack->size++;
   return;
}

char buffer[256]={0};   

void char_put(char ch)
{
    static int index=0;
    buffer[index++]=ch;
}

int priority(char ch)
{
    int ret=0;
    switch(ch)
    {
        case '+':
        case '-':
            ret=1;
            break;
        case '*':
        case '/':
            ret=2;
            break;
        default:
            break;
    }
    return ret;
}

int is_number(char ch)
{
    return(ch>='0'&&ch<='9');
}

int is_operator(char ch)
{
    return(ch=='+'||ch=='-'||ch=='*'||ch=='/');
}

int is_left(char ch)
{
    return(ch=='(');
}

int is_right(char ch)
{
    return(ch==')');
}

int transform(char str[])
{
    phead* istack=initstack();
    int i=0;
    while(str[i]!='\0')
    {
        
        if(is_number(str[i])==1)
        {
            if(is_number(str[i+1])==1)
            {
                char_put(str[i]);
            }
            else
            {
                char_put(str[i]);
                char_put(' ');
            }
        }
        else if(is_operator((str[i]))==1)
        {
            if(str[i+1]=='0'&&str[i]=='/')
            {
                printf("ILLEGAL");
                return 0;
            }
            if(isempty(istack)==0)
            {
                while((isempty(istack)==0)&&(priority(str[i])<=(priority(seqstack_top(istack)->val))))
                {
                    char_put(seqstack_pop(istack)->val);
                    char_put(' ');
                }
            }
            seqstack_push(istack,str[i]);
        }
        else if(is_left(str[i]))
        {
            seqstack_push(istack,str[i]);
        }
        else if(is_right(str[i]))
        {
            while(is_left(seqstack_top(istack)->val)!=1)
            {
                char_put(seqstack_pop(istack)->val);
                if(isempty(istack)==1)
                {
                    printf("Failed to match (\n");
                    return -1;
                }
            }
            
            seqstack_pop(istack);
            
        }
        else
        {
            printf("Illegal characters detected\n");
            return -1;
        }
        i++;
    }
    
    if(str[i]=='\0')
    {
        while(isempty(istack)==0)
        {
            if(seqstack_top(istack)->val=='(')
            {
                printf("Mismatched )\n");
                return -1;
            }
            char_put(seqstack_pop(istack)->val);
        }
    }
    else
    {
        printf("Traverse unfinished\n");
    }
    return 1;
}


typedef struct node1
{
    int val;
    struct node1* next;
}pnode1;

typedef struct seqstack1
{
    int size;
    pnode1* top;
}phead1;

phead1*  initstack1()
{
    phead1* istack=(phead1*)malloc(sizeof(phead1));
    if(istack!=NULL)
    {
        istack->top=NULL;
        istack->size=0;
    }
    return istack;
}

int isempty1(phead1* istack)
{
    if(istack->top==NULL)
    {
        return 1;
    }
    return 0;
}

int seqstack_top1(phead1* istack)
{
    if(istack->size!=0)
    {
        return istack->top->val;
    }
    return 99999;
}

int seqstack_pop1(phead1* istack)
{
    if(isempty1(istack)==0)
    {
        int account=istack->top->val;
        istack->top=istack->top->next;
        istack->size--;
        return account;
    }
    return 99999;
}

void seqstack_push1(phead1* istack,int x)
{
   pnode1* temp;
   temp=(pnode1*)malloc(sizeof(pnode1));
   temp->val=x;
   temp->next=istack->top;
   istack->top=temp;
   istack->size++;
   return;
}

int express(int left,int right,char op)
{
    switch (op)
    {
    case '+':
        return left+right;
    case '-':
        return left-right;
    case '*':
        return left*right;
    case '/':
        if(right==0)
        {
            return 999;
        }
        return left/right;
    default:
        break;
    }
    return -1;
}

int getsize(phead1* stack)
{
    return stack->size;
}

int calculate(char str[])
{
    phead1* istack2=initstack1();
    int i=0;
    while(str[i]!='\0')
    {
        char a[6]={0};
        int index=0;
        if(is_number(str[i])==1)
        {
            while(is_number(str[i])==1)
            {
                a[index]=str[i];
                index++;
                i++;
            }
            
            seqstack_push1(istack2,atoi(a));
        }
        else if(is_operator(str[i])==1)
        {
            int right=seqstack_pop1(istack2);
            int left=seqstack_pop1(istack2);
            int ret=express(left,right,str[i]);
            if(ret==999)
            {
                printf("ILLEGAL");
                return 999;
            }
            seqstack_push1(istack2,ret);
        }
        else if(str[i]==' ')
        {

        }
        else
        {
            printf("error\n");
            break;
        }
        i++;
    }
    if(str[i]=='\0'&&getsize(istack2))
    {
        return seqstack_top1(istack2);
    }
    return 0;
}

int main()
{
    char s[1024]={0};
    printf("Please type a math expression:\n");
    scanf("%s",s);
    int number=transform(s);
    if(number==-1)
    {
        printf("Failed to transform into Reverse Polish Notation.\n");
        return 0;
    }
 
    int num=calculate(buffer);
    if(num==999)
    {
        return 0;
    }
    printf("%d\n",num);
}
 