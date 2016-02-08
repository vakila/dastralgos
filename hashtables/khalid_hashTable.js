// suppose we have a hashmap/table that takes (key, values) of (String, Object)

function HashMap () {
    var array = [];
    array.length = 10;
    /**
     * Reduces a string to a numeric value, used for hash table internals
     * @param keyStr {String}
     * @returns {Integer}
     **/
    function hashCode (keyStr) {
        // reduce it to 1 integer ;=> which index to map the key to
        var result = Array.prototype.reduce.call(keyStr, (_hash, char) => {
            return _hash * 31 + char.charCodeAt(0);
        }, 7); // the default starting point is 7
        return result;
    }

    this.getVal = key => {
        return array[hashCode(key) % array.length];
    }

    this.setVal = function(key, value) {
        return array[hashCode(key) % array.length] = value;
    }
}
