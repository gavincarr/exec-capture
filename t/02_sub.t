# Basic exec-capture tests

use Test::More;
use Test::Files;
use IPC::Run3;
use FindBin qw($Bin);

my $dir = "$Bin/t02";
my $expected = "$dir/z1_status.expected";

my $outfile = "$dir/z1_status.out";
if (-f $outfile) {
  unlink $outfile or die "Cannot unlink $outfile: $!";
}

ok(run3([
  "$Bin/../exec-capture",
  '-N'      => 'z1_status.out',
  '-d'      => $dir,
  '--sub'   => 's/\b\d+(\.\d+)?\s*C\b/xxx C/g',
  '--sub'   => 's/\s-?\d+(\.\d+)?\s*dBm\b/ xxx dBm/g',
  'cat'     => "$dir/z1_status",
]), "run ok");
ok(-f $outfile, "output file $outfile created");
compare_ok($outfile, $expected, "output file $outfile munged correctly"); 

done_testing;

