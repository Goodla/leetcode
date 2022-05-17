class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        words = title.split()
        
        for i in range(len(words)):
            words[i] = words[i].lower()
            if len(words[i]) >= 3:
                words[i] = words[i][0].upper() + words[i][1:]
                
        r = ' '.join([str(elem) for elem in words])
        
        return r
