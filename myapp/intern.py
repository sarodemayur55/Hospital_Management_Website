check=0;
for(i=2;i<n;i++)
{
    if(n%i==0)
    {
        check=1
        break;
    }
}

if(check==1)
{
    print("is not prime")
}
else{
    print("is prime")
}

for(i=2;i<=n;i++)
{
    check=0;
    for(j=2;j<i;j++)
    {
        if(i%j==0)
        {
            check=1;
            break;
        }
    }
    if(check==0)
    {
        print(i);
    }
}