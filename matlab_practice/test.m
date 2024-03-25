clear
clc
close all;

[x,y] = ode('df',[-2,2],[3,4])

function dy = df(x,y)
dy = zeros(2,1)
dy(1)=dy(2)
dy(2)=2*x/(1+x*x)*y(2)
end


