module Main where

import Data.List
import Data.Char
import Data.Function

alphabet = ['a'..'z'] ++ ['A'..'Z'] -- а теперь сравним это с отсосами на других языках

alphalen = length alphabet

instCount :: String -> String -> Int
instCount a b = sum $ map fnd a
  where
    fnd c = length $ elemIndices c db
    db = map toLower b

anticaesar :: String -> [String]
anticaesar a = map shift [0..alphalen - 1]
  where
    shift nmb = map (shiftChar nmb) a
    shiftChar nmb char = case elemIndex char alphabet of
      Nothing -> char
      Just idx -> alphabet !! newidx
        where
          newidx = (idx + nmb) `mod` alphalen

main = getLine >>= (mapM_ putStrLn) . (take 10) . reverse . (sortBy (compare `on` (instCount "ao"))) . anticaesar

-- ghci anticaesar.hs
-- main
-- вводим текст