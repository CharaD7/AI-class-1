function [] = test_two_min()
z=[];
x= 0:0.1:30;
for n = x
    y = two_min(n);
    z=[z y];
end
plot(x,z);