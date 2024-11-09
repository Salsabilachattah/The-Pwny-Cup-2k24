package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func nothingLeft() {
	fmt.Println("wooooooooo Bye bYe ")
	return
}

func jackpot(input string) {
	car := strings.TrimSpace(input)
	if len(car) > 0 && car[0] == '}' {
		fmt.Println("Congratulations! you're the winner of the game")
	} else {
		fmt.Println("Close, but no .....")
	}
}

func caseOne(input string, no int) {
	fmt.Println("Unlocking case one!")

	if len(input) == 0 {
		nothingLeft()
		return
	}

	car := input[0]
	restOfString := input[1:]

	switch {

	case car == '3' && no == 1: //done shellmates{G0L4n9_15_3v3
		caseOne(restOfString, 0)

	case car == '!' && no == 2: //done shellmates{G0L4n9_15_3v3ry_ wh3r3!
		jackpot(restOfString)

	case car == 'a' && no == 5://done shellma
		caseTwo(restOfString, 1)

	case car == 'r' && no == 0: //done shellmates{G0L4n9_15_3v3r
		caseSix(restOfString, 1)
	
	case car == 's' && no == -1: //done s
		caseThree(restOfString, 1)	

	case car == 'm' && no == 3: //done shellm
		caseOne(restOfString, 5)	
	
	case car == '_' && no == 4: //done shellmates{G0L4n9_15_3v3ry_ 
		caseSix(restOfString, 2)	

	default:
		nothingLeft()
	}
}

func caseTwo(input string, no int) {
	fmt.Println("Unlocking case two!")

	if len(input) == 0 {
		nothingLeft()
		return
	}

	car := input[0]
	restOfString := input[1:]

	switch {
	case car == '3' && no == 4://done shellmates{G0L4n9_15_3
		caseTwo(restOfString, 6)

	case car == 'e' && no == 3: //done she
		caseTwo(restOfString, 2)

	case car == 'l' && no == 2: //done shel
		caseThree(restOfString, 2)
	

	case car == '9' && no == 5://done shellmates{G0L4n9
		caseThree(restOfString, 3)
	case car =='t' && no==1: //done shellmat
	    caseFive(restOfString,1)
	
	case car == 'v' && no == 6://done shellmates{G0L4n9_15_3v
			caseOne(restOfString, 1)
	

	default:
		nothingLeft()
	}
}

func caseThree(input string, no int) {
	fmt.Println("Unlocking case three!")

	if len(input) == 0 {
		nothingLeft()
		return
	}

	car := input[0]
	restOfString := input[1:]

	switch {
	case car == 'h' && no == 1: //done sh
		caseTwo(restOfString, 3)

	case car == 'G' && no == 4: // done shellmates{G
		caseFive(restOfString, 3)

	case car == '_' && no == 3://done shellmates{G0L4n9_
		caseFour(restOfString, 1)

	case car == 'l' && no == 2: //done shell
		caseOne(restOfString, 3)
	default:
		nothingLeft()
	}
}

func caseFour(input string, no int) {
	fmt.Println("Unlocking case four!")

	if len(input) == 0 {
		nothingLeft()
		return
	}

	car := input[0]
	restOfString := input[1:]

	switch {
	case car == '{' && no == 2: //done shellmates{
		caseThree(restOfString, 4)

	case car == 'L' && no == 5: //done shellmates{G0L
		caseFour(restOfString, 4)

	case car == '_' && no == 3://done shellmates{G0L4n9_15_
			caseTwo(restOfString, 4)

	case car == '1' && no == 1: //done shellmates{G0L4n9_1
		caseFive(restOfString, 2)

	case car == '4' && no == 4: //done shellmates{G0L4
		caseFive(restOfString, 4)

	default:
		nothingLeft()
	}
}

func caseFive(input string, no int) {
	fmt.Println("Unlocking case five!")

	if len(input) == 0 {
		nothingLeft()
		return
	}

	car := input[0]
	restOfString := input[1:]

	switch {
	case car == 'e' && no == 1://done shellmate
		caseFive(restOfString, 5)

	case car == '5' && no == 2://done shellmates{G0L4n9_15
		caseFour(restOfString, 3)	

	case car == 's' && no == 5: //done shellmates
		caseFour(restOfString, 2)

	case car == '0' && no == 3: //done shellmates{G0
		caseFour(restOfString, 5)

	case car == 'n' && no == 4: //done shellmates{G0L4n
		caseTwo(restOfString, 5)

	default:
		nothingLeft()
	}
}

func caseSix(input string, no int) {
	fmt.Println("Unlocking case Six!")

	if len(input) == 0 {
		nothingLeft()
		return
	}

	car := input[0]
	restOfString := input[1:]

	switch {
		case car == 'y' && no == 1: //done shellmates{G0L4n9_15_3v3ry
			caseOne(restOfString, 4)
		
		case car == 'w' && no == 2: //done shellmates{G0L4n9_15_3v3ry_w
			caseSix(restOfString, 3)

		case car == 'h' && no == 3: //done shellmates{G0L4n9_15_3v3ry_wh 
			caseSix(restOfString, 4)

		case car == '3' && no == 4: //done shellmates{G0L4n9_15_3v3ry_ wh3
			caseSix(restOfString, 5)

		case car == 'r' && no == 5: //done shellmates{G0L4n9_15_3v3ry_ wh3r
			caseSix(restOfString,6)	
		
		case car == '3' && no == 6: //done shellmates{G0L4n9_15_3v3ry_ wh3r3
			caseOne(restOfString, 2)					


	default:
		nothingLeft()
	}
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter The flag to win the game: ")
	input, _ := reader.ReadString('\n')
	input = strings.TrimSpace(input)

	if len(input) != 34 {
		fmt.Println("Hmmmmmmmmmm Okey ")
		return
	}

	caseOne(input, -1)
}
