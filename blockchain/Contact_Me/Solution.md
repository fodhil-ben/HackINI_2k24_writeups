# Contact Me
## Write up

we were given this solidity script
```
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;


contract Setup {
    bool public solved;

    constructor() payable {
        solved = false;
    }

    function makeACall(uint8 _hour) external {
        require(_hour == 7,"I'm not availabe at this hour, call me at 7.");
            solved = true;
    }

    function isSolved() public view returns (bool) {
        return solved == true;
    }

}
```
**Note**
>we were also given a website to launch an instance and get the contract address and private key and rpc url

to solve the challenge we must make the variable **solved** equals true and the only way is by calling the **makeACall** function and give it the argument 7

and we can easily do that 

**Note**
> to interact with this contract i used **foundry framework** so u must install it first

so the solution is just to call the makeAcall funtion and give it argument **7**

here is the command i used
```
cast send <contract address> "makeACall(uint8)" 7 --rpc-url <rpc-url> --private-key <private-key>
```

and you will get the flag after visiting the same website you used to get the rpc url and the private key

> flag : shellmates{U_c0ntRACteDm3$ucce$sFullY_0x007}
