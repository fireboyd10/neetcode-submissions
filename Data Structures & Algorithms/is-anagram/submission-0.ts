class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s: string, t: string): boolean {
        if (s.length !== t.length)
            return false;
        let count = {};

        for (let i = 0; i < s.length; i++){
            let letter = s[i];
            if (!count[letter])
                count[letter] = 1;
            else count[letter]++;
        }

        for (let j = 0; j < t.length; j++){
            let letter = t[j];
            
            if (count[letter] === undefined)
                return false;
            if (count[letter]<1)
                return false;
            count[letter]--;
        }

        return true;
    }
}
