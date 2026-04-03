# Anagram Solver & Game

A full-stack web application built with **FastAPI, React (TypeScript), PostgreSQL, and Docker**.

It started from a classic LeetCode problem (grouping anagrams) and evolved into:
- an API-based solver
- a persistent database of words
- a small interactive anagram game with scoring

---

## Features

### Anagram Solver
- Input a list of words
- Groups them into anagrams
- Stores normalized words and keys in PostgreSQL

Example:
["eat","tea","tan","ate","nat","bat"]  → [["bat"],["nat","tan"],["ate","eat","tea"]]

### Anagram Game
- Get a random word from stored anagrams
- Submit another valid anagram
-  validated against DB or dictionary API
- If correct:
  -  user receives points
- New valid words are persisted
