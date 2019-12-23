from pathlib import Path
projectRootPath = Path('../')
testPath = projectRootPath / 'ahoj'
if not Path.exists(testPath):
	testPath.mkdir(exist_ok=True)