def find_king_status(pieces):
    pieces = pieces.strip(" ").strip("\n").split(" ")
    unsafe_positions = set()
    kingLoc = (0, 0)
    alphaNum = {"abcdefgh"[i]:i for i in range(8)}
    positionValid = lambda r, c: 0 <= r < 8 and 0 <= c < 8
    occupied = set()
    for piece in pieces:
        pieceType, rLoc, cLoc = piece[0], 8 - int(piece[2]), alphaNum[piece[1]]
        if pieceType == "K": continue
        occupied.add((rLoc, cLoc))

    for piece in pieces:
        pieceType, rLoc, cLoc = piece[0], 8-int(piece[2]), alphaNum[piece[1]]
        if pieceType == "K":
            kingLoc = (rLoc, cLoc)
            continue
        elif pieceType == "Q":
            # everything in row is unsafe
            for c in range(cLoc + 1, 8):
                if (rLoc, c) in occupied:
                    unsafe_positions.add((rLoc, c))
                    break
                unsafe_positions.add((rLoc, c))
            for c in range(cLoc - 1, -1, -1):
                if (rLoc, c) in occupied:
                    unsafe_positions.add((rLoc, c))
                    break
                unsafe_positions.add((rLoc, c))
            # everything in col is unsafe
            for r in range(rLoc + 1, 8):
                if (r, cLoc) in occupied:
                    unsafe_positions.add((r, cLoc))
                    break
                unsafe_positions.add((r, cLoc))
            for r in range(rLoc - 1, -1, -1):
                if (r, cLoc) in occupied:
                    unsafe_positions.add((r, cLoc))
                    break
                unsafe_positions.add((r, cLoc))
            # everything in / diag is unsafe
            for r in range(rLoc + 1, 8):
                if (r, rLoc + cLoc - r) in occupied:
                    unsafe_positions.add((r, rLoc + cLoc - r))
                    break
                unsafe_positions.add((r, rLoc + cLoc - r))
            for r in range(rLoc - 1, -1, -1):
                if (r, rLoc + cLoc - r) in occupied:
                    unsafe_positions.add((r, rLoc + cLoc - r))
                    break
                unsafe_positions.add((r, rLoc + cLoc - r))
            # everything in \ diag is unsafe
            for r in range(rLoc + 1, 8):
                c = r + cLoc - rLoc
                if (r, c) in occupied:
                    unsafe_positions.add((r, c))
                    break
                unsafe_positions.add((r, c))
            for r in range(rLoc - 1, -1, -1):
                c = r + cLoc - rLoc
                if (r, c) in occupied:
                    unsafe_positions.add((r, c))
                    break
                unsafe_positions.add((r, c))
        elif pieceType == "R":
            # everything in row is unsafe
            for c in range(cLoc + 1, 8):
                if (rLoc, c) in occupied:
                    unsafe_positions.add((rLoc, c))
                    break
                unsafe_positions.add((rLoc, c))
            for c in range(cLoc - 1, -1, -1):
                if (rLoc, c) in occupied:
                    unsafe_positions.add((rLoc, c))
                    break
                unsafe_positions.add((rLoc, c))
            # everything in col is unsafe
            for r in range(rLoc + 1, 8):
                if (r, cLoc) in occupied:
                    unsafe_positions.add((r, cLoc))
                    break
                unsafe_positions.add((r, cLoc))
            for r in range(rLoc - 1, -1, -1):
                if (r, cLoc) in occupied:
                    unsafe_positions.add((r, cLoc))
                    break
                unsafe_positions.add((r, cLoc))
        elif pieceType == "B":
            # everything in / diag is unsafe
            for r in range(rLoc + 1, 8):
                if (r, rLoc + cLoc - r) in occupied:
                    unsafe_positions.add((r, rLoc + cLoc - r))
                    break
                unsafe_positions.add((r, rLoc + cLoc - r))
            for r in range(rLoc - 1, -1, -1):
                if (r, rLoc + cLoc - r) in occupied:
                    unsafe_positions.add((r, rLoc + cLoc - r))
                    break
                unsafe_positions.add((r, rLoc + cLoc - r))
            # everything in \ diag is unsafe
            for r in range(rLoc + 1, 8):
                c = r + cLoc - rLoc
                if (r, c) in occupied:
                    unsafe_positions.add((r, c))
                    break
                unsafe_positions.add((r, c))
            for r in range(rLoc - 1, -1, -1):
                c = r + cLoc - rLoc
                if (r, c) in occupied:
                    unsafe_positions.add((r, c))
                    break
                unsafe_positions.add((r, c))
        elif pieceType == "P":
            # if (rLoc-1, cLoc-1) not in occupied:
            unsafe_positions.add((rLoc-1, cLoc-1))
            # if (rLoc-1, cLoc+1) not in occupied:
            unsafe_positions.add((rLoc-1, cLoc+1))
        elif pieceType == "N":
            knightDirs = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
            for k in knightDirs:
                # if (rLoc+k[0], cLoc+k[1]) not in occupied:
                unsafe_positions.add((rLoc+k[0], cLoc+k[1]))
                # 5 7 8
    # Check for four possible states of king
    kingCanMove = False
    for dR in [-1, 0, 1]:
        for dC in [-1, 0, 1]:
            nR, nC = kingLoc[0]+dR, kingLoc[1]+dC
            if not positionValid(nR, nC) or (dR == 0 and dC == 0): continue
            if (nR, nC) not in unsafe_positions:
                kingCanMove = True
                break
        else: continue
        break
    kingSafeCurrently = kingLoc not in unsafe_positions
    if kingSafeCurrently and kingCanMove: return "SAFE"
    elif kingSafeCurrently and not kingCanMove: return "STALEMATE"
    elif not kingSafeCurrently and kingCanMove: return "CHECK"
    else: return "CHECKMATE"
