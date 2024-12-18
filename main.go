package main

import (
	"fmt"
	"net/http"
	"os"

	"github.com/github/testdatabot/handlers"
)

func main() {
	if err := run(); err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
}

func run() error {
	http.HandleFunc("/random-commit-message", handlers.CommitMessage)
	http.HandleFunc("/random-lorem-ipsum", handlers.Loripsum)
	http.HandleFunc("/random-user", handlers.User)
	http.HandleFunc("/weather", handlers.Weather)
	http.HandleFunc("/joke", handlers.Joke)
	http.HandleFunc("/capital-city", handlers.CapitalCity)
	http.HandleFunc("/_ping", func(w http.ResponseWriter, r *http.Request) {
		w.Write([]byte("OK"))
	})

	http.ListenAndServe(":8080", nil)
	return nil
}
