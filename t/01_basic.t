# Basic exec-capture tests

use Test::More;
use Test::Files;
use File::Path qw(remove_tree);
use IPC::Run3;
use FindBin qw($Bin);

my $dir = "t01";

if (-d "$Bin/$dir") {
  remove_tree("$Bin/$dir") or die "remove_tree failed: $!";
}

ok(run3([ "$Bin/../exec-capture", '-d', $dir, qw(echo1 echo one two three) ]), "run ok");
ok(-f "$Bin/$dir/echo1", 'output file echo1 created');
file_ok("$Bin/$dir/echo1", "one two three\n", 'echo1 file contains correct output');

done_testing;

