class Solution(object):
    def numberOfBeams(self, bank):
        if len(bank) < 2:
            return 0

        solution = 0
        beacons_in_prev_row = 0
        beacons_in_current_row = 0
        for row in bank:
            beacons_in_current_row = 0
            for c in row:
                if c == '1':
                    beacons_in_current_row += 1
            solution += beacons_in_current_row * beacons_in_prev_row
            beacons_in_prev_row = beacons_in_current_row or beacons_in_prev_row

        return solution