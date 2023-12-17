# Interstellar
## Write up

we were given two files

**Setup.sol**

```
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.7.0;

import {SpaceShip} from "./SpaceShip.sol";

contract Setup {
    SpaceShip public immutable TARGET;

    constructor() payable {
        TARGET = new SpaceShip();
    }


    function isSolved() public view returns (bool) {
        return TARGET.getDistanceTraveled() == 0;
    }
}
```


**SpaceShip.sol**
```
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.7.0;

contract SpaceShip {
    uint32 public distanceFromTheBlackHole;
    uint32 private distanceTraveled;

    constructor() {
        distanceTraveled = 1337;
        distanceFromTheBlackHole = 4294967295;
    }

    function galacticBoost(uint32 advanceWithDistance) public {
        // Avoid the space ship from falling into the black hole
        require(distanceTraveled + advanceWithDistance < distanceFromTheBlackHole);
        distanceTraveled += advanceWithDistance;
    }

    
    function getDistanceTraveled() public view returns (uint256) {
        return distanceTraveled;
    }

}
```


to solve this challenge we must set the distanceTraveled variable to 0
the variable gets initialized to 1337 and it is declared as uint32 
there is this function **galacticBoost** we can call to add distance but we want to make it zero so is that possible
this version of solidity is vulnerable to integer overlflow 
uint32 meens that the biggest number that it can stores will be 32 bit
so (2 ** 32) - 1

but what if we pass to it a number so that when it does **distanceTraveled + advanceWithDistance**
the result will be greater the 2 ** 32 - 1 

it will overflow beacuse it depassed the 32 bit limit

so **distanceTraveled + advanceWithDistance** will be set to 0 first and then it will add the rest

and **distanceTraveled += advanceWithDistance;**
will overflow to reach zero and then start counting again

so that is the solution 

we will add this number so when it add it it will pass the 32 bit number it will be 0
2 ** 32-1337

here is a simple example of integer overflow

    (2 ** 32) - 1 = 0b11111111111111111111111111111111
+
    1             = 0b00000000000000000000000000000001
    ---------------------------------------------------
    ============== 0b100000000000000000000000000000000


    1337 =          0b00000000000000000000010100111001
+
    (2 ** 32) - 1 = 0b11111111111111111111111111111111
    ---------------------------------------------------
    ============== 0b100000000000000000000010100111000


so by adding (2 ** 32) - 1 it actually got reseted to 0 and then add the rest which is 1336

so what if we do 

    1337 =             0b00000000000000000000010100111001
+
    (2 ** 32) - 1337 = 0b11111111111111111111101011000111
    ---------------------------------------------------
    ==============    0b100000000000000000000000000000000

so adding (2 ** 32) - 1337 will result in distanceTraveled = 0

so we get the flag 

here is the solution using cast command:

first step:
get the spaceship contract address 
```
cast call <setup contract address> "TARGET()(address)" --rpc-url <rpc-url> 
```

second step: 
call the **galacticBoost** function with argument (2 ** 32) - 1337  = 4294965959

```
cast send <SpaceShip contract address> "galacticBoost(uint32)" 4294965959 --rpc-url <rpc url> --private-key <private key>
```

and we get the flag

> flag : shellmates{1nt3g3R_0v3rfl0o0W_1s_4_Bl0o0o0cKk_H0o0l3}